#!/usr/bin/env python
# camcops_server/tasks/cape42.py

"""
===============================================================================

    Copyright (C) 2012-2018 Rudolf Cardinal (rudolf@pobox.com).

    This file is part of CamCOPS.

    CamCOPS is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    CamCOPS is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with CamCOPS. If not, see <http://www.gnu.org/licenses/>.

===============================================================================
"""

from typing import Any, Dict, List, Optional, Tuple, Type

import cardinal_pythonlib.rnc_web as ws
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.sql.sqltypes import Float, Integer

from camcops_server.cc_modules.cc_db import add_multiple_columns
from camcops_server.cc_modules.cc_html import answer, tr
from camcops_server.cc_modules.cc_request import CamcopsRequest
from camcops_server.cc_modules.cc_summaryelement import SummaryElement
from camcops_server.cc_modules.cc_task import Task, TaskHasPatientMixin
from camcops_server.cc_modules.cc_trackerhelpers import TrackerInfo


# =============================================================================
# CAPE-42
# =============================================================================

QUESTION_SNIPPETS = [
    # 1-10
    "sad", "double meaning", "not very animated", "not a talker",
    "magazines/TV personal", "some people not what they seem",
    "persecuted", "few/no emotions", "pessimistic", "conspiracy",
    # 11-20
    "destined for importance", "no future", "special/unusual person",
    "no longer want to live", "telepathy", "no interest being with others",
    "electrical devices influence thinking", "lacking motivation",
    "cry about nothing", "occult",
    # 21-30
    "lack energy", "people look oddly because of appearance", "mind empty",
    "thoughts removed", "do nothing", "thoughts not own",
    "feelings lacking intensity", "others might hear thoughts",
    "lack spontaneity", "thought echo",
    # 31-40
    "controlled by other force", "emotions blunted", "hear voices",
    "hear voices conversing", "neglecting appearance/hygiene",
    "never get things done", "few hobbies/interests", "feel guilty",
    "feel a failure", "tense",
    # 41-42
    "Capgras", "see things others cannot"
]
NQUESTIONS = 42
POSITIVE = [2, 5, 6, 7, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 30, 31, 33,
            34, 41, 42]
DEPRESSIVE = [1, 9, 12, 14, 19, 38, 39, 40]
NEGATIVE = [3, 4, 8, 16, 18, 21, 23, 25, 27, 29, 32, 35, 36, 37]
ALL = list(range(1, NQUESTIONS + 1))
MIN_SCORE_PER_Q = 1
MAX_SCORE_PER_Q = 4

ALL_MIN = MIN_SCORE_PER_Q * NQUESTIONS
ALL_MAX = MAX_SCORE_PER_Q * NQUESTIONS
POS_MIN = MIN_SCORE_PER_Q * len(POSITIVE)
POS_MAX = MAX_SCORE_PER_Q * len(POSITIVE)
NEG_MIN = MIN_SCORE_PER_Q * len(NEGATIVE)
NEG_MAX = MAX_SCORE_PER_Q * len(NEGATIVE)
DEP_MIN = MIN_SCORE_PER_Q * len(DEPRESSIVE)
DEP_MAX = MAX_SCORE_PER_Q * len(DEPRESSIVE)

DP = 2


class Cape42Metaclass(DeclarativeMeta):
    # noinspection PyInitNewSignature
    def __init__(cls: Type['Cape42'],
                 name: str,
                 bases: Tuple[Type, ...],
                 classdict: Dict[str, Any]) -> None:
        add_multiple_columns(
            cls, "frequency", 1, NQUESTIONS,
            minimum=MIN_SCORE_PER_Q, maximum=MAX_SCORE_PER_Q,
            comment_fmt=(
                "Q{n} ({s}): frequency? (1 never, 2 sometimes, 3 often, "
                "4 nearly always)"
            ),
            comment_strings=QUESTION_SNIPPETS
        )
        add_multiple_columns(
            cls, "distress", 1, NQUESTIONS,
            minimum=MIN_SCORE_PER_Q, maximum=MAX_SCORE_PER_Q,
            comment_fmt=(
                "Q{n} ({s}): distress (1 not, 2 a bit, 3 quite, 4 very), if "
                "frequency > 1"
            ),
            comment_strings=QUESTION_SNIPPETS)
        super().__init__(name, bases, classdict)


class Cape42(TaskHasPatientMixin, Task,
             metaclass=Cape42Metaclass):
    __tablename__ = "cape42"
    shortname = "CAPE-42"
    longname = "Community Assessment of Psychic Experiences"
    provides_trackers = True

    def get_trackers(self, req: CamcopsRequest) -> List[TrackerInfo]:
        fstr1 = "CAPE-42 weighted frequency score: "
        dstr1 = "CAPE-42 weighted distress score: "
        wtr = " ({low}–{high})".format(
            low=MIN_SCORE_PER_Q,
            high=MAX_SCORE_PER_Q)
        fstr2 = " weighted freq. score" + wtr
        dstr2 = " weighted distress score" + wtr
        axis_min = MIN_SCORE_PER_Q - 0.2
        axis_max = MAX_SCORE_PER_Q + 0.2
        return [
            TrackerInfo(
                value=self.weighted_frequency_score(ALL),
                plot_label=fstr1 + "overall",
                axis_label="Overall" + fstr2,
                axis_min=axis_min,
                axis_max=axis_max
            ),
            TrackerInfo(
                value=self.weighted_distress_score(ALL),
                plot_label=dstr1 + "overall",
                axis_label="Overall" + dstr2,
                axis_min=axis_min,
                axis_max=axis_max,
            ),
            TrackerInfo(
                value=self.weighted_frequency_score(POSITIVE),
                plot_label=fstr1 + "positive symptoms",
                axis_label="Positive Sx" + fstr2,
                axis_min=axis_min,
                axis_max=axis_max
            ),
            TrackerInfo(
                value=self.weighted_distress_score(POSITIVE),
                plot_label=dstr1 + "positive symptoms",
                axis_label="Positive Sx" + dstr2,
                axis_min=axis_min,
                axis_max=axis_max
            ),
            TrackerInfo(
                value=self.weighted_frequency_score(NEGATIVE),
                plot_label=fstr1 + "negative symptoms",
                axis_label="Negative Sx" + fstr2,
                axis_min=axis_min,
                axis_max=axis_max,
            ),
            TrackerInfo(
                value=self.weighted_distress_score(NEGATIVE),
                plot_label=dstr1 + "negative symptoms",
                axis_label="Negative Sx" + dstr2,
                axis_min=axis_min,
                axis_max=axis_max,
            ),
            TrackerInfo(
                value=self.weighted_frequency_score(DEPRESSIVE),
                plot_label=fstr1 + "depressive symptoms",
                axis_label="Depressive Sx" + fstr2,
                axis_min=axis_min,
                axis_max=axis_max,
            ),
            TrackerInfo(
                value=self.weighted_distress_score(DEPRESSIVE),
                plot_label=dstr1 + "depressive symptoms",
                axis_label="Depressive Sx" + dstr2,
                axis_min=axis_min,
                axis_max=axis_max,
            ),
        ]

    def get_summaries(self, req: CamcopsRequest) -> List[SummaryElement]:
        wtr = " ({low}-{high})".format(
            low=MIN_SCORE_PER_Q,
            high=MAX_SCORE_PER_Q)
        return self.standard_task_summary_fields() + [
            SummaryElement(
                name="all_freq", coltype=Integer(),
                value=self.frequency_score(ALL),
                comment=(
                    "Total score = frequency score for all questions "
                    "({low}-{high})".format(low=ALL_MIN, high=ALL_MAX))),
            SummaryElement(
                name="all_distress", coltype=Integer(),
                value=self.distress_score(ALL),
                comment=(
                    "Distress score for all questions "
                    "({low}-{high})".format(low=ALL_MIN, high=ALL_MAX))),

            SummaryElement(
                name="positive_frequency", coltype=Integer(),
                value=self.frequency_score(POSITIVE),
                comment=(
                    "Frequency score for positive symptom questions "
                    "({low}-{high})".format(low=POS_MIN, high=POS_MAX))),
            SummaryElement(
                name="positive_distress", coltype=Integer(),
                value=self.distress_score(POSITIVE),
                comment=(
                    "Distress score for positive symptom questions "
                    "({low}-{high})".format(low=POS_MIN, high=POS_MAX))),

            SummaryElement(
                name="negative_frequency", coltype=Integer(),
                value=self.frequency_score(NEGATIVE),
                comment=(
                    "Frequency score for negative symptom questions "
                    "({low}-{high})".format(low=NEG_MIN, high=NEG_MAX))),
            SummaryElement(
                name="negative_distress", coltype=Integer(),
                value=self.distress_score(NEGATIVE),
                comment=(
                    "Distress score for negative symptom questions "
                    "({low}-{high})".format(low=NEG_MIN, high=NEG_MAX))),

            SummaryElement(
                name="depressive_frequency", coltype=Integer(),
                value=self.frequency_score(DEPRESSIVE),
                comment=(
                    "Frequency score for depressive symptom questions "
                    "({low}-{high})".format(low=DEP_MIN, high=DEP_MAX))),
            SummaryElement(
                name="depressive_distress", coltype=Integer(),
                value=self.distress_score(DEPRESSIVE),
                comment=(
                    "Distress score for depressive symptom questions "
                    "({low}-{high})".format(low=DEP_MIN, high=DEP_MAX))),

            SummaryElement(
                name="wt_all_freq", coltype=Float(),
                value=self.weighted_frequency_score(ALL),
                comment="Weighted frequency score: overall" + wtr),
            SummaryElement(
                name="wt_all_distress", coltype=Float(),
                value=self.weighted_distress_score(ALL),
                comment="Weighted distress score: overall" + wtr),

            SummaryElement(
                name="wt_pos_freq", coltype=Float(),
                value=self.weighted_frequency_score(POSITIVE),
                comment="Weighted frequency score: positive symptoms" + wtr),
            SummaryElement(
                name="wt_pos_distress", coltype=Float(),
                value=self.weighted_distress_score(POSITIVE),
                comment="Weighted distress score: positive symptoms" + wtr),

            SummaryElement(
                name="wt_neg_freq", coltype=Float(),
                value=self.weighted_frequency_score(NEGATIVE),
                comment="Weighted frequency score: negative symptoms" + wtr),
            SummaryElement(
                name="wt_neg_distress", coltype=Float(),
                value=self.weighted_distress_score(NEGATIVE),
                comment="Weighted distress score: negative symptoms" + wtr),

            SummaryElement(
                name="wt_dep_freq", coltype=Float(),
                value=self.weighted_frequency_score(DEPRESSIVE),
                comment="Weighted frequency score: depressive symptoms" + wtr),
            SummaryElement(
                name="wt_dep_distress", coltype=Float(),
                value=self.weighted_distress_score(DEPRESSIVE),
                comment="Weighted distress score: depressive symptoms" + wtr),
        ]

    def is_question_complete(self, q: int) -> bool:
        f = self.get_frequency(q)
        if f is None:
            return False
        if f > 1 and self.get_distress(q) is None:
            return False
        return True

    def is_complete(self) -> bool:
        if not self.field_contents_valid():
            return False
        for q in ALL:
            if not self.is_question_complete(q):
                return False
        return True

    def get_frequency(self, q: int) -> Optional[int]:
        return getattr(self, "frequency" + str(q))

    def get_distress(self, q: int) -> Optional[int]:
        return getattr(self, "distress" + str(q))

    def get_distress_score(self, q: int) -> Optional[int]:
        if not self.endorsed(q):
            return MIN_SCORE_PER_Q
        return self.get_distress(q)

    def endorsed(self, q: int) -> bool:
        f = self.get_frequency(q)
        return f is not None and f > MIN_SCORE_PER_Q

    def distress_score(self, qlist: List[int]) -> int:
        score = 0
        for q in qlist:
            d = self.get_distress_score(q)
            if d is not None:
                score += d
        return score

    def frequency_score(self, qlist: List[int]) -> int:
        score = 0
        for q in qlist:
            f = self.get_frequency(q)
            if f is not None:
                score += f
        return score

    def weighted_frequency_score(self, qlist: List[int]) -> Optional[float]:
        score = 0
        n = 0
        for q in qlist:
            f = self.get_frequency(q)
            if f is not None:
                score += f
                n += 1
        if n == 0:
            return None
        return score / n

    def weighted_distress_score(self, qlist: List[int]) -> Optional[float]:
        score = 0
        n = 0
        for q in qlist:
            f = self.get_frequency(q)
            d = self.get_distress_score(q)
            if f is not None and d is not None:
                score += d
                n += 1
        if n == 0:
            return None
        return score / n

    @staticmethod
    def question_category(q: int) -> str:
        if q in POSITIVE:
            return "P"
        if q in NEGATIVE:
            return "N"
        if q in DEPRESSIVE:
            return "D"
        return "?"

    def get_task_html(self, req: CamcopsRequest) -> str:
        h = """
            <div class="summary">
                <table class="summary">
                    {iscomplete}
                </table>
                <table class="summary">
                    <tr>
                        <th>Domain (with score range)</th>
                        <th>Frequency (total score)</th>
                        <th>Distress (total score)</th>
                    </tr>
        """.format(iscomplete=self.get_is_complete_tr(req))

        h += tr(
            "Overall <sup>[1]</sup> ({low}–{high})".format(
                low=ALL_MIN,
                high=ALL_MAX),
            self.frequency_score(ALL),
            self.distress_score(ALL))
        h += tr(
            "Positive symptoms ({low}–{high})".format(
                low=POS_MIN,
                high=POS_MAX),
            self.frequency_score(POSITIVE),
            self.distress_score(POSITIVE))
        h += tr(
            "Negative symptoms ({low}–{high})".format(
                low=NEG_MIN,
                high=NEG_MAX),
            self.frequency_score(NEGATIVE),
            self.distress_score(NEGATIVE))
        h += tr(
            "Depressive symptoms ({low}–{high})".format(
                low=DEP_MIN,
                high=DEP_MAX),
            self.frequency_score(DEPRESSIVE),
            self.distress_score(DEPRESSIVE))

        h += """
                </table>
                <table class="summary">
                    <tr>
                        <th>Domain</th>
                        <th>Weighted frequency score <sup>[3]</sup></th>
                        <th>Weighted distress score <sup>[3]</sup></th>
                    </tr>
        """

        h += tr("Overall ({n} questions)".format(n=len(ALL)),
                ws.number_to_dp(self.weighted_frequency_score(ALL), DP),
                ws.number_to_dp(self.weighted_distress_score(ALL), DP))
        h += tr("Positive symptoms ({n} questions)".format(n=len(POSITIVE)),
                ws.number_to_dp(self.weighted_frequency_score(POSITIVE), DP),
                ws.number_to_dp(self.weighted_distress_score(POSITIVE), DP))
        h += tr("Negative symptoms ({n} questions)".format(n=len(NEGATIVE)),
                ws.number_to_dp(self.weighted_frequency_score(NEGATIVE), DP),
                ws.number_to_dp(self.weighted_distress_score(NEGATIVE), DP))
        h += tr(
            "Depressive symptoms ({n} questions)".format(n=len(DEPRESSIVE)),
            ws.number_to_dp(self.weighted_frequency_score(DEPRESSIVE), DP),
            ws.number_to_dp(self.weighted_distress_score(DEPRESSIVE), DP))

        h += """
                </table>
            </div>
            <div class="explanation">
                FREQUENCY: 1 {f1}, 2 {f2}, 3 {f3}, 4 {f4}.
                DISTRESS: 1 {d1}, 2 {d2}, 3 {d3}, 4 {d4}.
            </div>
            <table class="taskdetail">
                <tr>
                    <th width="70%">
                        Question (P positive, N negative, D depressive)
                    </th>
                    <th width="15%">Frequency ({low}–{high})</th>
                    <th width="15%">Distress ({low}–{high}) <sup>[2]</sup></th>
                </tr>
        """.format(
            f1=self.wxstring(req, "frequency_option1"),
            f2=self.wxstring(req, "frequency_option2"),
            f3=self.wxstring(req, "frequency_option3"),
            f4=self.wxstring(req, "frequency_option4"),
            d1=self.wxstring(req, "distress_option1"),
            d2=self.wxstring(req, "distress_option2"),
            d3=self.wxstring(req, "distress_option3"),
            d4=self.wxstring(req, "distress_option4"),
            low=MIN_SCORE_PER_Q,
            high=MAX_SCORE_PER_Q,
        )
        for q in ALL:
            h += tr(
                "{q}. ".format(q=q) +
                self.wxstring(req, "q" + str(q)) +
                " (<i>" + self.question_category(q) + "</i>)",
                answer(self.get_frequency(q)),
                answer(
                    self.get_distress_score(q) if self.endorsed(q) else None,
                    default=str(MIN_SCORE_PER_Q))
            )
        h += """
            </table>
            <div class="footnotes">
                [1] “Total” score is the overall frequency score (the sum of
                frequency scores for all questions).
                [2] Distress coerced to 1 if frequency is 1.
                [3] Sum score per dimension divided by number of completed
                items. Shown to {dp} decimal places. Will be in the range
                {low}–{high}, or blank if not calculable.
            </div>
        """.format(
            low=MIN_SCORE_PER_Q,
            high=MAX_SCORE_PER_Q,
            dp=DP,
        )
        return h
