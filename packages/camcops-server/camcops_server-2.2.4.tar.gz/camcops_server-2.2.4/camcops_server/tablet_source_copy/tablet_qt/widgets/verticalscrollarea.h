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

#include <QScrollArea>
#include <QSize>
class QGestureEvent;
class QSwipeGesture;

// http://forum.qt.io/topic/13374/solved-qscrollarea-vertical-scroll-only/4


class VerticalScrollArea : public QScrollArea
{
    // Contains objects in a vertical scroll area.
    // - Inheritance: QScrollArea : QAbstractScrollArea : QFrame : QWidget
    // - Note that it *contains* a QWidget, named 'qt_scrollarea_viewport',
    //   which has the user-inserted widget as its child. This has the same
    //   implications with respect to height-for-width (and height generally?)
    //   as for BaseWidget (q.v.).
    // - Internally, this is "QWidget* viewport". However, it is in the private
    //   class, accessed via the standard Qt private pointer, so inaccessible.

    Q_OBJECT
public:
    explicit VerticalScrollArea(QWidget* parent = nullptr);
    virtual bool event(QEvent* event) override;
    virtual bool eventFilter(QObject* o, QEvent* e) override;
    virtual QSize sizeHint() const override;
    virtual void resizeEvent(QResizeEvent* event) override;
    void setWidget(QWidget* widget);  // hides parent version
protected:
    void resetSizeLimits();
    bool gestureEvent(QGestureEvent* event);
    void swipeTriggered(QSwipeGesture* gesture);
protected:
    int m_last_widget_width;
    int m_reentry_depth;
    QSize m_widget_size_back_1;
    QSize m_widget_size_back_2;
};
