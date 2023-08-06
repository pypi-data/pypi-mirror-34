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

#include "quverticalcontainer.h"
#include <QWidget>
#include "layouts/layouts.h"
#include "lib/sizehelpers.h"
#include "questionnairelib/questionnaire.h"
#include "widgets/basewidget.h"

const Qt::Alignment QuVerticalContainer::DefaultWidgetAlignment = Qt::AlignLeft | Qt::AlignVCenter;


QuVerticalContainer::QuVerticalContainer()
{
}


QuVerticalContainer::QuVerticalContainer(const QVector<QuElementPtr>& elements,
                                         const Qt::Alignment alignment) :
    m_elements(elements)
{
    createAlignments(alignment);
}


QuVerticalContainer::QuVerticalContainer(
        std::initializer_list<QuElementPtr> elements,
        const Qt::Alignment alignment) :
    m_elements(elements)
{
    createAlignments(alignment);
}


QuVerticalContainer::QuVerticalContainer(
        std::initializer_list<QuElement*> elements,
        const Qt::Alignment alignment)  // takes ownership
{
    for (auto e : elements) {
        addElement(e, alignment);
    }
}


QuVerticalContainer* QuVerticalContainer::addElement(
        const QuElementPtr& element,
        const Qt::Alignment alignment)
{
    m_elements.append(element);
    m_widget_alignments.append(alignment);
    return this;
}


QuVerticalContainer* QuVerticalContainer::addElement(
        QuElement* element,   // takes ownership
        const Qt::Alignment alignment)
{
    // If you add a nullptr, it will be ignored.
    if (element) {
        m_elements.append(QuElementPtr(element));
        m_widget_alignments.append(alignment);
    }
    return this;
}


QuVerticalContainer* QuVerticalContainer::setWidgetAlignment(
        const Qt::Alignment alignment)
{
    createAlignments(alignment);
    return this;
}


void QuVerticalContainer::createAlignments(const Qt::Alignment alignment)
{
    m_widget_alignments.clear();
    for (int i = 0; i < m_elements.size(); ++i) {
        m_widget_alignments.append(alignment);
    }
}


QPointer<QWidget> QuVerticalContainer::makeWidget(Questionnaire* questionnaire)
{
    QPointer<QWidget> widget(new BaseWidget());
    widget->setSizePolicy(sizehelpers::expandingFixedHFWPolicy());

    VBoxLayout* layout = new VBoxLayout();

    // widget->setObjectName(CssConst::DEBUG_YELLOW);
    layout->setContentsMargins(uiconst::NO_MARGINS);
    widget->setLayout(layout);
    for (int i = 0; i < m_elements.size(); ++i) {
        auto e = m_elements.at(i);
        auto alignment = m_widget_alignments.at(i);
        QPointer<QWidget> w = e->widget(questionnaire);
        layout->addWidget(w, 0, alignment);
    }
    return widget;
}


QVector<QuElementPtr> QuVerticalContainer::subelements() const
{
    return m_elements;
}
