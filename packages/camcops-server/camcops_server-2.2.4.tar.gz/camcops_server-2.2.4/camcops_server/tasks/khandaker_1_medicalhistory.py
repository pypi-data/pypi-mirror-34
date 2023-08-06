#!/usr/bin/env python
# camcops_server/tasks/khandaker_1_medicalhistory.py

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

from typing import Any, Dict, Tuple, Type

import cardinal_pythonlib.rnc_web as ws
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import UnicodeText

from camcops_server.cc_modules.cc_html import (
    bold,
    get_yes_no_none,
    tr_span_col,
)
from camcops_server.cc_modules.cc_request import CamcopsRequest
from camcops_server.cc_modules.cc_sqla_coltypes import BoolColumn
from camcops_server.cc_modules.cc_task import Task, TaskHasPatientMixin


class KQInfo(object):
    def __init__(self, stem: str, heading_xml: str = "") -> None:
        self.fieldname_yn = stem + "_yn"
        self.fieldname_comment = stem + "_comment"
        self.question_xmlstr = "q_" + stem
        self.heading_xmlstr = heading_xml
        
    def has_heading(self) -> bool:
        return bool(self.heading_xmlstr)


QUESTIONS = [
    KQInfo("cancer", "heading_cancer"),
    KQInfo("epilepsy", "heading_brain"),
    KQInfo("cva_headinjury_braintumour"),
    KQInfo("ms_pd_dementia"),
    KQInfo("cerebralpalsy_otherbrain"),
    KQInfo("visual_impairment"),
    KQInfo("heart_disorder", "heading_cardiovascular"),
    KQInfo("respiratory", "heading_respiratory"),
    KQInfo("gastrointestinal", "heading_gastrointestinal"),
    KQInfo("other_inflammatory", "heading_inflammatory"),
    KQInfo("musculoskeletal", "heading_musculoskeletal"),
    KQInfo("renal_urinary", "heading_renal_urinary"),
    KQInfo("dermatological", "heading_dermatological"),
    KQInfo("diabetes", "heading_endocrinological"),
    KQInfo("other_endocrinological"),
    KQInfo("haematological", "heading_haematological"),
    KQInfo("infections", "heading_infections"),
]

X_TITLE = "title"
X_INSTRUCTION = "instruction"
X_HEADING_CONDITION = "heading_condition"
X_HEADING_YN = "heading_yn"
X_HEADING_COMMENT = "heading_comment"
X_COMMENT_HINT = "comment_hint"


# =============================================================================
# Khandaker_1_MedicalHistory
# =============================================================================

class Khandaker1MedicalHistoryMetaclass(DeclarativeMeta):
    # noinspection PyInitNewSignature
    def __init__(cls: Type['Khandaker1MedicalHistory'],
                 name: str,
                 bases: Tuple[Type, ...],
                 classdict: Dict[str, Any]) -> None:
        for qinfo in QUESTIONS:
            setattr(cls, qinfo.fieldname_yn, BoolColumn(qinfo.fieldname_yn))
            setattr(cls, qinfo.fieldname_comment,
                    Column(qinfo.fieldname_comment, UnicodeText))
        super().__init__(name, bases, classdict)


class Khandaker1MedicalHistory(TaskHasPatientMixin, Task,
                               metaclass=Khandaker1MedicalHistoryMetaclass):
    __tablename__ = "khandaker_1_medicalhistory"
    shortname = "Khandaker_1_MedicalHistory"
    longname = "Khandaker GM — 1 — Insight — Medical history"

    def is_complete(self) -> bool:
        for qinfo in QUESTIONS:
            yn_value = getattr(self, qinfo.fieldname_yn)
            if yn_value is None:
                return False
            if yn_value:
                comment = getattr(self, qinfo.fieldname_comment)
                if not comment:
                    return False
        return True

    def get_task_html(self, req: CamcopsRequest) -> str:
        html = """
            <div class="summary">
                <table class="summary">
                    {is_complete_tr}
                </table>
            </div>
            <table class="taskdetail">
                <tr>
                    <th width="40%">{condition}</th>
                    <th width="20%">{yn}</th>
                    <th width="40%">{comment}</th>
                </tr>
        """.format(
            is_complete_tr=self.get_is_complete_tr(req),
            condition=self.xstring(req, X_HEADING_CONDITION),
            yn=self.xstring(req, X_HEADING_YN),
            comment=self.xstring(req, X_HEADING_COMMENT),
        )

        for qinfo in QUESTIONS:
            if qinfo.has_heading():
                html += tr_span_col(
                    self.xstring(req, qinfo.heading_xmlstr),
                    cols=3,
                    tr_class="subheading",
                )
            yn_value = getattr(self, qinfo.fieldname_yn)
            yn_str = get_yes_no_none(req, yn_value)
            if yn_value:
                yn_str = bold(yn_str)
            comment_value = getattr(self, qinfo.fieldname_comment)
            html += """
                <tr>
                    <td>{question}</td>
                    <td>{yn}</td>
                    <td>{comment}</td>
                </tr>
            """.format(
                question=self.xstring(req, qinfo.question_xmlstr),
                yn=yn_str,
                comment=(
                    bold(ws.webify(comment_value)) if comment_value else ""
                ),
            )

        html += "</table>"
        return html
