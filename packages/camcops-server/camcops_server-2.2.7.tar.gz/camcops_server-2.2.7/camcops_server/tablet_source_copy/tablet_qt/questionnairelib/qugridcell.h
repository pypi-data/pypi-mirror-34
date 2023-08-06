/*
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
*/

#pragma once
#include "questionnairelib/quelement.h"


class QuGridCell
{
    // Encapsulates a grid cell containing a QuElement.
    // Used by QuContainerGrid.

public:
    QuGridCell();  // so it can live in a QVector
    QuGridCell(const QuElementPtr element,
               int row,  // y position, starting from 0, going down
               int column,  // x position, starting from 0, going right
               int row_span = 1,   // height
               int column_span = 1,  // width
               Qt::Alignment alignment = 0);
    QuGridCell(QuElement* element,  // takes ownership
               int row,
               int column,
               int row_span = 1,
               int column_span = 1,
               Qt::Alignment alignment = 0);
public:
    QuElementPtr element;
    int row;
    int column;
    int row_span;
    int column_span;
    Qt::Alignment alignment;
    // http://doc.qt.io/qt-5.7/qgridlayout.html
public:
    friend QDebug operator<<(QDebug debug, const QuGridCell& plan);
};
