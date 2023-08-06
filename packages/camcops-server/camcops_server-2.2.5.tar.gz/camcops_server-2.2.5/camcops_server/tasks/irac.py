#!/usr/bin/env python
# camcops_server/tasks/irac.py

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

import cardinal_pythonlib.rnc_web as ws

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, UnicodeText

from camcops_server.cc_modules.cc_html import tr_qa
from camcops_server.cc_modules.cc_request import CamcopsRequest
from camcops_server.cc_modules.cc_sqla_coltypes import (
    CamcopsColumn,
    ZERO_TO_TWO_CHECKER,
)
from camcops_server.cc_modules.cc_task import (
    get_from_dict,
    Task,
    TaskHasPatientMixin,
)


# =============================================================================
# IRAC
# =============================================================================

class Irac(TaskHasPatientMixin, Task):
    __tablename__ = "irac"
    shortname = "IRAC"
    longname = "Identify and Rate the Aim of the Contact"

    aim = Column(
        "aim", UnicodeText,
        comment="Main aim of the contact"
    )
    achieved = CamcopsColumn(
        "achieved", Integer,
        permitted_value_checker=ZERO_TO_TWO_CHECKER,
        comment="Was the aim achieved? (0 not, 1 partially, 2 fully)"
    )

    TASK_FIELDS = ["aim", "achieved"]

    def is_complete(self) -> bool:
        return (self.are_all_fields_complete(self.TASK_FIELDS) and
                self.field_contents_valid())

    def get_achieved_text(self, req: CamcopsRequest) -> str:
        achieveddict = {
            None: None,
            0: self.wxstring(req, "achieved_0"),
            1: self.wxstring(req, "achieved_1"),
            2: self.wxstring(req, "achieved_2"),
        }
        return get_from_dict(achieveddict, self.achieved)

    def get_task_html(self, req: CamcopsRequest) -> str:
        if self.achieved is not None:
            achieved = "{}. {}".format(self.achieved,
                                       self.get_achieved_text(req))
        else:
            achieved = None
        h = """
            <div class="summary">
                <table class="summary">
        """ + self.get_is_complete_tr(req) + """
                </table>
            </div>
            <table class="taskdetail">
                <tr>
                    <th width="50%">Question</th>
                    <th width="50%">Answer</th>
                </tr>
        """
        h += tr_qa(self.wxstring(req, "q_aim"), ws.webify(self.aim))
        h += tr_qa(self.wxstring(req, "q_achieved"), achieved)
        h += """
            </table>
        """
        return h
