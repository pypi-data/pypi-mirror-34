# ActivitySim
# See full license in LICENSE.txt.

import os
import logging

import numpy as np
import pandas as pd

from activitysim.core import simulate
from activitysim.core import tracing
from activitysim.core import pipeline
from activitysim.core import config
from activitysim.core import inject
from activitysim.core import logit

from activitysim.core.util import assign_in_place

from .util import expressions
from activitysim.core.util import reindex
from .util.overlap import person_time_window_overlap

logger = logging.getLogger(__name__)


@inject.injectable()
def joint_tour_participation_spec(configs_dir):
    return simulate.read_model_spec(configs_dir, 'joint_tour_participation.csv')


def joint_tour_participation_candidates(joint_tours, persons_merged):

    # - only interested in persons from households with joint_tours
    persons_merged = persons_merged[persons_merged.num_hh_joint_tours > 0]

    # person_cols = ['household_id', 'PNUM', 'ptype', 'adult', 'travel_active']
    # household_cols = ['num_hh_joint_tours', 'home_is_urban', 'home_is_rural',
    #                   'car_sufficiency', 'income_in_thousands',
    #                   'num_adults', 'num_children', 'num_travel_active',
    #                   'num_travel_active_adults', 'num_travel_active_children']
    # persons_merged = persons_merged[person_cols + household_cols]

    # - create candidates table
    candidates = pd.merge(
        joint_tours.reset_index().rename(columns={'person_id': 'point_person_id'}),
        persons_merged.reset_index().rename(columns={persons_merged.index.name: 'person_id'}),
        left_on=['household_id'], right_on=['household_id'])

    # should have all joint_tours
    assert len(candidates['tour_id'].unique()) == joint_tours.shape[0]

    # - filter out ineligible candidates (adults for children-only tours, and vice-versa)
    eligible = ~(
        ((candidates.composition == 'adults') & ~candidates.adult) |
        ((candidates.composition == 'children') & candidates.adult)
    )
    candidates = candidates[eligible]

    # - stable (predictable) index
    MAX_PNUM = 100
    if candidates.PNUM.max() > MAX_PNUM:
        # if this happens, channel random seeds will overlap at MAX_PNUM (not probably a big deal)
        logger.warn("max persons.PNUM (%s) > MAX_PNUM (%s)" % (candidates.PNUM.max(), MAX_PNUM))

    candidates['participant_id'] = (candidates[joint_tours.index.name] * MAX_PNUM) + candidates.PNUM
    candidates.set_index('participant_id', drop=True, inplace=True, verify_integrity=True)

    return candidates


def get_tour_satisfaction(candidates, participate):

    tour_ids = candidates.tour_id.unique()

    if participate.any():

        candidates = candidates[participate]

        # if this happens, we would need to filter them out!
        assert not ((candidates.composition == 'adults') & ~candidates.adult).any()
        assert not ((candidates.composition == 'children') & candidates.adult).any()

        cols = ['tour_id', 'composition', 'adult']

        # tour satisfaction
        x = candidates[cols].groupby(['tour_id', 'composition']).adult.agg(['size', 'sum']).\
            reset_index('composition').rename(columns={'size': 'participants', 'sum': 'adults'})

        satisfaction = (x.composition != 'mixed') & (x.participants > 1) | \
                       (x.composition == 'mixed') & (x.adults > 0) & (x.participants > x.adults)

        satisfaction = satisfaction.reindex(tour_ids).fillna(False).astype(bool)

    else:
        satisfaction = pd.Series([])

    # ensure we return a result for every joint tour, even if no participants
    satisfaction = satisfaction.reindex(tour_ids).fillna(False).astype(bool)

    return satisfaction


def participants_chooser(probs, choosers, spec, trace_label):
    """
    custom alternative to logit.make_choices for simulate.simple_simulate

    Choosing participants for mixed tours is trickier than adult or child tours becuase we
    need at least one adult and one child participant in a mixed tour. We call logit.make_choices
    and then check to see if the tour statisfies this requirement, and rechoose for any that
    fail until all are satisfied.

    In principal, this shold always occur eventually, but we fail after MAX_ITERATIONS,
    just in case there is some failure in program logic (haven't seen this occur.)

    Parameters
    ----------
    probs : pandas.DataFrame
        Rows for choosers and columns for the alternatives from which they
        are choosing. Values are expected to be valid probabilities across
        each row, e.g. they should sum to 1.
    choosers : pandas.dataframe
        simple_simulate choosers df
    spec : pandas.DataFrame
        simple_simulate spec df
        We only need spec so we can know the column index of the 'participate' alternative
        indicating that the participant has been chosen to participate in the tour
    trace_label : str

    Returns - same as logit.make_choices
    -------
    choices, rands
        choices, rands as returned by logit.make_choices (in same order as probs)

    """

    assert probs.index.equals(choosers.index)

    # choice is boolean (participate or not)
    model_settings = config.read_model_settings('joint_tour_participation.yaml')

    choice_col = model_settings.get('participation_choice', 'participate')
    assert choice_col in spec.columns, \
        "couldn't find participation choice column '%s' in spec"
    PARTICIPATE_CHOICE = spec.columns.get_loc(choice_col)
    MAX_ITERATIONS = model_settings.get('max_participation_choice_iterations', 5000)

    trace_label = tracing.extend_trace_label(trace_label, 'participants_chooser')

    candidates = choosers.copy()
    choices_list = []
    rands_list = []

    num_tours_remaining = len(candidates.tour_id.unique())
    logger.info('%s %s joint tours to satisfy.' % (trace_label, num_tours_remaining,))

    iter = 0
    while candidates.shape[0] > 0:

        iter += 1

        if iter > MAX_ITERATIONS:
            logger.warn('%s max iterations exceeded (%s).' % (trace_label, MAX_ITERATIONS))
            diagnostic_cols = ['tour_id', 'household_id', 'composition', 'adult']
            unsatisfied_candidates = candidates[diagnostic_cols].join(probs)
            tracing.write_csv(unsatisfied_candidates,
                              file_name='%s.UNSATISFIED' % trace_label, transpose=False)
            print unsatisfied_candidates.head(20)
            assert False

        choices, rands = logit.make_choices(probs, trace_label=trace_label, trace_choosers=choosers)
        participate = (choices == PARTICIPATE_CHOICE)

        # satisfaction indexed by tour_id
        tour_satisfaction = get_tour_satisfaction(candidates, participate)
        num_tours_satisfied_this_iter = tour_satisfaction.sum()

        if num_tours_satisfied_this_iter > 0:

            num_tours_remaining -= num_tours_satisfied_this_iter

            satisfied = reindex(tour_satisfaction, candidates.tour_id)

            choices_list.append(choices[satisfied])
            rands_list.append(rands[satisfied])

            # remove candidates of satisfied tours
            probs = probs[~satisfied]
            candidates = candidates[~satisfied]

        logger.info('%s iteration %s : %s joint tours satisfied %s remaining' %
                    (trace_label, iter, num_tours_satisfied_this_iter, num_tours_remaining,))

    choices = pd.concat(choices_list)
    rands = pd.concat(rands_list).reindex(choosers.index)

    # reindex choices and rands to match probs and v index
    choices = choices.reindex(choosers.index)
    rands = rands.reindex(choosers.index)
    assert choices.index.equals(choosers.index)
    assert rands.index.equals(choosers.index)

    logger.info('%s %s iterations to satisfy all joint tours.' % (trace_label, iter,))

    return choices, rands


def add_null_results(trace_label):
    logger.info("Skipping %s: joint tours" % trace_label)
    # participants table is used downstream in non-joint tour expressions
    participants = pd.DataFrame(columns=['person_id'])
    participants.index.name = 'participant_id'
    pipeline.replace_table("joint_tour_participants", participants)


@inject.step()
def joint_tour_participation(
        tours, persons_merged,
        joint_tour_participation_spec,
        chunk_size,
        trace_hh_id):
    """
    Predicts for each eligible person to participate or not participate in each joint tour.
    """
    trace_label = 'joint_tour_participation'
    model_settings = config.read_model_settings('joint_tour_participation.yaml')

    tours = tours.to_frame()
    joint_tours = tours[tours.tour_category == 'joint']

    # - if no joint tours
    if joint_tours.shape[0] == 0:
        add_null_results(trace_label)
        return

    persons_merged = persons_merged.to_frame()

    # - create joint_tour_participation_candidates table
    candidates = joint_tour_participation_candidates(joint_tours, persons_merged)
    tracing.register_traceable_table('participants', candidates)
    pipeline.get_rn_generator().add_channel(candidates, 'joint_tour_participants')

    logger.info("Running joint_tours_participation with %d potential participants (candidates)" %
                candidates.shape[0])

    # - preprocessor
    preprocessor_settings = model_settings.get('preprocessor', None)
    if preprocessor_settings:

        locals_dict = {
            'person_time_window_overlap': person_time_window_overlap,
            'persons': persons_merged
        }

        expressions.assign_columns(
            df=candidates,
            model_settings=preprocessor_settings,
            locals_dict=locals_dict,
            trace_label=trace_label)

    # - simple_simulate

    nest_spec = config.get_logit_model_settings(model_settings)
    constants = config.get_model_constants(model_settings)

    choices = simulate.simple_simulate(
        choosers=candidates,
        spec=joint_tour_participation_spec,
        nest_spec=nest_spec,
        locals_d=constants,
        chunk_size=chunk_size,
        trace_label=trace_label,
        trace_choice_name='participation',
        custom_chooser=participants_chooser)

    # choice is boolean (participate or not)
    choice_col = model_settings.get('participation_choice', 'participate')
    assert choice_col in joint_tour_participation_spec.columns, \
        "couldn't find participation choice column '%s' in spec"
    PARTICIPATE_CHOICE = joint_tour_participation_spec.columns.get_loc(choice_col)

    participate = (choices == PARTICIPATE_CHOICE)

    # satisfaction indexed by tour_id
    tour_satisfaction = get_tour_satisfaction(candidates, participate)

    assert tour_satisfaction.all()

    candidates['satisfied'] = reindex(tour_satisfaction, candidates.tour_id)

    PARTICIPANT_COLS = ['tour_id', 'household_id', 'person_id']
    participants = candidates[participate][PARTICIPANT_COLS].copy()

    # assign participant_num
    # FIXME do we want something smarter than the participant with the lowest person_id?
    participants['participant_num'] = \
        participants.sort_values(by=['tour_id', 'person_id']).\
        groupby('tour_id').cumcount() + 1

    pipeline.replace_table("joint_tour_participants", participants)

    # FIXME drop channel if we aren't using any more?
    # pipeline.get_rn_generator().drop_channel('joint_tours_participants')

    # - assign joint tour 'point person' (participant_num == 1)
    point_persons = participants[participants.participant_num == 1]
    joint_tours['person_id'] = point_persons.set_index('tour_id').person_id

    # update number_of_participants which was initialized to 1
    joint_tours['number_of_participants'] = participants.groupby('tour_id').size()

    assign_in_place(tours, joint_tours[['person_id', 'number_of_participants']])

    pipeline.replace_table("tours", tours)

    if trace_hh_id:
        tracing.trace_df(participants,
                         label="joint_tour_participation.participants")

        tracing.trace_df(joint_tours,
                         label="joint_tour_participation.joint_tours")
