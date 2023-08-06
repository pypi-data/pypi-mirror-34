#!/usr/bin/env python
# camcops_server/tasks/pdss.py

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

import cardinal_pythonlib.rnc_web as ws
from cardinal_pythonlib.stringfunc import strseq
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.sql.sqltypes import Float, Integer

from camcops_server.cc_modules.cc_constants import DATA_COLLECTION_UNLESS_UPGRADED_DIV  # noqa
from camcops_server.cc_modules.cc_ctvinfo import CTV_INCOMPLETE, CtvInfo
from camcops_server.cc_modules.cc_db import add_multiple_columns
from camcops_server.cc_modules.cc_html import answer, tr
from camcops_server.cc_modules.cc_request import CamcopsRequest
from camcops_server.cc_modules.cc_summaryelement import SummaryElement
from camcops_server.cc_modules.cc_task import Task, TaskHasPatientMixin
from camcops_server.cc_modules.cc_trackerhelpers import TrackerInfo


# =============================================================================
# PDSS
# =============================================================================

DP = 3


class PdssMetaclass(DeclarativeMeta):
    # noinspection PyInitNewSignature
    def __init__(cls: Type['Pdss'],
                 name: str,
                 bases: Tuple[Type, ...],
                 classdict: Dict[str, Any]) -> None:
        add_multiple_columns(
            cls, "q", 1, cls.NQUESTIONS,
            minimum=cls.MIN_PER_Q, maximum=cls.MAX_PER_Q,
            comment_fmt="Q{n}, {s} (0-4, higher worse)",
            comment_strings=[
                "frequency",
                "distressing during",
                "anxiety about panic",
                "places or situations avoided",
                "activities avoided",
                "interference with responsibilities",
                "interference with social life",
            ]
        )
        super().__init__(name, bases, classdict)


class Pdss(TaskHasPatientMixin, Task,
           metaclass=PdssMetaclass):
    __tablename__ = "pdss"
    shortname = "PDSS"
    longname = "Panic Disorder Severity Scale"
    provides_trackers = True

    MIN_PER_Q = 0
    MAX_PER_Q = 4
    NQUESTIONS = 7
    QUESTION_FIELDS = strseq("q", 1, NQUESTIONS)
    MAX_TOTAL = MAX_PER_Q * NQUESTIONS
    MAX_COMPOSITE = 4

    def get_trackers(self, req: CamcopsRequest) -> List[TrackerInfo]:
        return [TrackerInfo(
            value=self.total_score(),
            plot_label="PDSS total score (lower is better)",
            axis_label="Total score (out of {})".format(self.MAX_TOTAL),
            axis_min=-0.5,
            axis_max=self.MAX_TOTAL + 0.5
        )]

    def get_summaries(self, req: CamcopsRequest) -> List[SummaryElement]:
        return self.standard_task_summary_fields() + [
            SummaryElement(
                name="total_score", coltype=Integer(),
                value=self.total_score(),
                comment="Total score (/ {})".format(self.MAX_TOTAL)
            ),
            SummaryElement(
                name="composite_score", coltype=Float(),
                value=self.composite_score(),
                comment="Composite score (/ {})".format(self.MAX_COMPOSITE)
            ),
        ]

    def get_clinical_text(self, req: CamcopsRequest) -> List[CtvInfo]:
        if not self.is_complete():
            return CTV_INCOMPLETE
        t = self.total_score()
        c = ws.number_to_dp(self.composite_score(), DP, default="?")
        return [CtvInfo(
            content="PDSS total score {t}/{mt} (composite {c}/{mc})".format(
                t=t,
                mt=self.MAX_TOTAL,
                c=c,
                mc=self.MAX_COMPOSITE
            )
        )]

    def total_score(self) -> int:
        return self.sum_fields(self.QUESTION_FIELDS)

    def composite_score(self) -> int:
        return self.mean_fields(self.QUESTION_FIELDS)

    def is_complete(self) -> bool:
        return (
            self.field_contents_valid() and
            self.are_all_fields_complete(self.QUESTION_FIELDS)
        )

    def get_task_html(self, req: CamcopsRequest) -> str:
        h = """
            <div class="summary">
                <table class="summary">
                    {complete_tr}
                    <tr>
                        <td>Total score</td>
                        <td>{total} / {tmax}</td>
                    </td>
                    <tr>
                        <td>Composite (mean) score</td>
                        <td>{composite} / {cmax}</td>
                    </td>
                </table>
            </div>
            <table class="taskdetail">
                <tr>
                    <th width="60%">Question</th>
                    <th width="40%">Answer ({qmin}–{qmax})</th>
                </tr>
        """.format(
            complete_tr=self.get_is_complete_tr(req),
            total=answer(self.total_score()),
            tmax=self.MAX_TOTAL,
            composite=answer(ws.number_to_dp(self.composite_score(), DP,
                                             default="?")),
            cmax=self.MAX_COMPOSITE,
            qmin=self.MIN_PER_Q,
            qmax=self.MAX_PER_Q,
        )
        for q in range(1, self.NQUESTIONS + 1):
            qtext = self.wxstring(req, "q" + str(q))
            a = getattr(self, "q" + str(q))
            atext = (self.wxstring(req, "q{}_option{}".format(q, a), str(a))
                     if a is not None else None)
            h += tr(qtext, answer(atext))
        h += """
            </table>
        """ + DATA_COLLECTION_UNLESS_UPGRADED_DIV
        return h
