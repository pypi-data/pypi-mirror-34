#!/usr/bin/env python
# camcops_server/tasks/panss.py

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

from typing import Any, Dict, List, Tuple, Type

from cardinal_pythonlib.stringfunc import strseq
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.sql.sqltypes import Integer

from camcops_server.cc_modules.cc_constants import DATA_COLLECTION_ONLY_DIV
from camcops_server.cc_modules.cc_ctvinfo import CTV_INCOMPLETE, CtvInfo
from camcops_server.cc_modules.cc_db import add_multiple_columns
from camcops_server.cc_modules.cc_html import tr_qa
from camcops_server.cc_modules.cc_request import CamcopsRequest
from camcops_server.cc_modules.cc_summaryelement import SummaryElement
from camcops_server.cc_modules.cc_task import (
    get_from_dict,
    Task,
    TaskHasClinicianMixin,
    TaskHasPatientMixin,
)
from camcops_server.cc_modules.cc_trackerhelpers import TrackerInfo


# =============================================================================
# PANSS
# =============================================================================

class PanssMetaclass(DeclarativeMeta):
    # noinspection PyInitNewSignature
    def __init__(cls: Type['Panss'],
                 name: str,
                 bases: Tuple[Type, ...],
                 classdict: Dict[str, Any]) -> None:
        add_multiple_columns(
            cls, "p", 1, cls.NUM_P,
            minimum=1, maximum=7,
            comment_fmt="P{n}: {s} (1 absent - 7 extreme)",
            comment_strings=[
                "delusions", "conceptual disorganisation",
                "hallucinatory behaviour", "excitement",
                "grandiosity", "suspiciousness/persecution",
                "hostility",
            ]
        )
        add_multiple_columns(
            cls, "n", 1, cls.NUM_N,
            minimum=1, maximum=7,
            comment_fmt="N{n}: {s} (1 absent - 7 extreme)",
            comment_strings=[
                "blunted affect", "emotional withdrawal",
                "poor rapport", "passive/apathetic social withdrawal",
                "difficulty in abstract thinking",
                "lack of spontaneity/conversation flow",
                "stereotyped thinking",
            ]
        )
        add_multiple_columns(
            cls, "g", 1, cls.NUM_G,
            minimum=1, maximum=7,
            comment_fmt="G{n}: {s} (1 absent - 7 extreme)",
            comment_strings=[
                "somatic concern",
                "anxiety",
                "guilt feelings",
                "tension",
                "mannerisms/posturing",
                "depression",
                "motor retardation",
                "uncooperativeness",
                "unusual thought content",
                "disorientation",
                "poor attention",
                "lack of judgement/insight",
                "disturbance of volition",
                "poor impulse control",
                "preoccupation",
                "active social avoidance",
            ]
        )
        super().__init__(name, bases, classdict)


class Panss(TaskHasPatientMixin, TaskHasClinicianMixin, Task,
            metaclass=PanssMetaclass):
    __tablename__ = "panss"
    shortname = "PANSS"
    longname = "Positive and Negative Syndrome Scale"
    provides_trackers = True

    NUM_P = 7
    NUM_N = 7
    NUM_G = 16

    P_FIELDS = strseq("p", 1, NUM_P)
    N_FIELDS = strseq("n", 1, NUM_N)
    G_FIELDS = strseq("g", 1, NUM_G)
    TASK_FIELDS = P_FIELDS + N_FIELDS + G_FIELDS

    MIN_P = 1 * NUM_P
    MAX_P = 7 * NUM_P
    MIN_N = 1 * NUM_N
    MAX_N = 7 * NUM_N
    MIN_G = 1 * NUM_G
    MAX_G = 7 * NUM_G
    MIN_TOTAL = MIN_P + MIN_N + MIN_G
    MAX_TOTAL = MAX_P + MAX_N + MAX_G
    MIN_P_MINUS_N = MIN_P - MAX_N
    MAX_P_MINUS_N = MAX_P - MIN_N

    def get_trackers(self, req: CamcopsRequest) -> List[TrackerInfo]:
        return [
            TrackerInfo(
                value=self.total_score(),
                plot_label="PANSS total score",
                axis_label="Total score ({}-{})".format(
                    self.MIN_TOTAL, self.MAX_TOTAL),
                axis_min=self.MIN_TOTAL - 0.5,
                axis_max=self.MAX_TOTAL + 0.5
            ),
            TrackerInfo(
                value=self.score_p(),
                plot_label="PANSS P score",
                axis_label="P score ({}-{})".format(self.MIN_P, self.MAX_P),
                axis_min=self.MIN_P - 0.5,
                axis_max=self.MAX_P + 0.5
            ),
            TrackerInfo(
                value=self.score_n(),
                plot_label="PANSS N score",
                axis_label="N score ({}-{})".format(self.MIN_N, self.MAX_N),
                axis_min=self.MIN_N - 0.5,
                axis_max=self.MAX_N + 0.5
            ),
            TrackerInfo(
                value=self.score_g(),
                plot_label="PANSS G score",
                axis_label="G score ({}-{})".format(self.MIN_G, self.MAX_G),
                axis_min=self.MIN_G - 0.5,
                axis_max=self.MAX_G + 0.5
            ),
            TrackerInfo(
                value=self.composite(),
                plot_label="PANSS composite score ({} to {})".format(
                    self.MIN_P_MINUS_N, self.MAX_P_MINUS_N),
                axis_label="P - N"
            ),
        ]

    def get_clinical_text(self, req: CamcopsRequest) -> List[CtvInfo]:
        if not self.is_complete():
            return CTV_INCOMPLETE
        return [CtvInfo(
            content=(
                "PANSS total score {} (P {}, N {}, G {}, "
                "composite P–N {})".format(
                    self.total_score(),
                    self.score_p(),
                    self.score_n(),
                    self.score_g(),
                    self.composite()
                )
            )
        )]

    def get_summaries(self, req: CamcopsRequest) -> List[SummaryElement]:
        return self.standard_task_summary_fields() + [
            SummaryElement(
                name="total",
                coltype=Integer(),
                value=self.total_score(),
                comment="Total score ({}-{})".format(
                    self.MIN_TOTAL, self.MAX_TOTAL)
            ),
            SummaryElement(
                name="p",
                coltype=Integer(),
                value=self.score_p(),
                comment="Positive symptom (P) score ({}-{})".format(
                    self.MIN_P, self.MAX_P)
            ),
            SummaryElement(
                name="n",
                coltype=Integer(),
                value=self.score_n(),
                comment="Negative symptom (N) score ({}-{})".format(
                    self.MIN_N, self.MAX_N)
            ),
            SummaryElement(
                name="g",
                coltype=Integer(),
                value=self.score_g(),
                comment="General symptom (G) score ({}-{})".format(
                    self.MIN_G, self.MAX_G)
            ),
            SummaryElement(
                name="composite",
                coltype=Integer(),
                value=self.composite(),
                comment="Composite score (P - N) ({} to {})".format(
                    self.MIN_P_MINUS_N, self.MAX_P_MINUS_N)
            ),
        ]

    def is_complete(self) -> bool:
        return (
            self.are_all_fields_complete(self.TASK_FIELDS) and
            self.field_contents_valid()
        )

    def total_score(self) -> int:
        return self.sum_fields(self.TASK_FIELDS)

    def score_p(self) -> int:
        return self.sum_fields(self.P_FIELDS)

    def score_n(self) -> int:
        return self.sum_fields(self.N_FIELDS)

    def score_g(self) -> int:
        return self.sum_fields(self.G_FIELDS)

    def composite(self) -> int:
        return self.score_p() - self.score_n()

    def get_task_html(self, req: CamcopsRequest) -> str:
        p = self.score_p()
        n = self.score_n()
        g = self.score_g()
        composite = self.composite()
        total = p + n + g
        answers = {
            None: None,
            1: self.wxstring(req, "option1"),
            2: self.wxstring(req, "option2"),
            3: self.wxstring(req, "option3"),
            4: self.wxstring(req, "option4"),
            5: self.wxstring(req, "option5"),
            6: self.wxstring(req, "option6"),
            7: self.wxstring(req, "option7"),
        }
        h = """
            <div class="summary">
                <table class="summary">
        """
        h += self.get_is_complete_tr(req)
        h += tr_qa("{} ({}–{})".format(req.wappstring("total_score"),
                                       self.MIN_TOTAL, self.MAX_TOTAL),
                   total)
        h += tr_qa("{} ({}–{})".format(self.wxstring(req, "p"),
                                       self.MIN_P, self.MAX_P),
                   p)
        h += tr_qa("{} ({}–{})".format(self.wxstring(req, "n"),
                                       self.MIN_N, self.MAX_N),
                   n)
        h += tr_qa("{} ({}–{})".format(self.wxstring(req, "g"),
                                       self.MIN_G, self.MAX_G),
                   g)
        h += tr_qa("{} ({}–{})".format(self.wxstring(req, "composite"),
                                       self.MIN_P_MINUS_N, self.MAX_P_MINUS_N),
                   composite)
        h += """
                </table>
            </div>
            <table class="taskdetail">
                <tr>
                    <th width="40%">Question</th>
                    <th width="60%">Answer</th>
                </tr>
        """
        for q in self.TASK_FIELDS:
            h += tr_qa(
                self.wxstring(req, "" + q + "_s"),
                get_from_dict(answers, getattr(self, q))
            )
        h += """
            </table>
        """ + DATA_COLLECTION_ONLY_DIV
        return h
