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
#include <QColor>
#include <QWidget>


class FixedAreaHfwTestWidget : public QWidget
{
    Q_OBJECT
public:
    FixedAreaHfwTestWidget(int area = 50000,
                           int preferred_width = 1000,
                           const QColor& background_colour = QColor(0, 0, 255),
                           int border_thickness = 0,
                           const QColor& border_colour = QColor(255, 0, 0),
                           const QColor& text_colour = QColor(255, 0, 255),
                           QWidget* parent = nullptr);
    virtual QSize sizeHint() const override;
    virtual bool hasHeightForWidth() const override;
    virtual int heightForWidth(int width) const override;
    virtual void paintEvent(QPaintEvent* event);
protected:
    int m_area;
    int m_preferred_width;
    QColor m_background_colour;
    int m_border_thickness;
    QColor m_border_colour;
    QColor m_text_colour;
    int m_min_area;
    int m_max_area;
};
