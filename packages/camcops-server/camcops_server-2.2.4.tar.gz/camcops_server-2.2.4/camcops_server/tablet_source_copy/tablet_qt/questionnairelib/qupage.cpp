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

#include "qupage.h"
#include <QWidget>
#include "db/fieldref.h"
#include "layouts/layouts.h"
#include "widgets/basewidget.h"


QuPage::QuPage()
{
    commonConstructor();
}


QuPage::QuPage(const QVector<QuElementPtr>& elements) :
    m_elements(elements)
{
    commonConstructor();
}


QuPage::QuPage(std::initializer_list<QuElementPtr> elements) :
    m_elements(elements)
{
    commonConstructor();
}


void QuPage::commonConstructor()
{
    m_type = PageType::Inherit;
    m_skip = false;
    m_allow_scroll = true;
    m_progress_blocked = false;
}


QuPage::QuPage(const QVector<QuElement*>& elements)  // takes ownership
{
    for (auto e : elements) {
        addElement(e);
    }
    commonConstructor();
}


QuPage::QuPage(std::initializer_list<QuElement*> elements)  // takes ownership
{
    for (auto e : elements) {
        addElement(e);
    }
    commonConstructor();
}


QuPage::~QuPage()
{
}


QuPage* QuPage::setType(const PageType type)
{
    m_type = type;
    return this;
}


QuPage* QuPage::setTitle(const QString& title)
{
    m_title = title;
    return this;
}


QuPage* QuPage::setSkip(const bool skip)
{
    m_skip = skip;
    return this;
}


QuPage* QuPage::addElement(const QuElementPtr& element)
{
    m_elements.append(element);
    return this;
}


QuPage* QuPage::addElement(QuElement* element)  // takes ownership
{
    // If you add a nullptr, it will be ignored.
    if (element) {
        addElement(QuElementPtr(element));
    }
    return this;
}


QuPage* QuPage::addElements(const QVector<QuElementPtr>& elements)
{
    for (auto e : elements) {
        addElement(e);
    }
    return this;
}


QuPage* QuPage::addElements(const QVector<QuElement*>& elements)
{
    for (auto e : elements) {
        addElement(e);
    }
    return this;
}


void QuPage::clearElements()
{
    m_elements.clear();
}


QuPage* QuPage::allowScroll(const bool allow_scroll)
{
    m_allow_scroll = allow_scroll;
    return this;
}


bool QuPage::allowsScroll() const
{
    return m_allow_scroll;
}


QuPage* QuPage::addTag(const QString& tag)
{
    m_tags.append(tag);
    return this;
}


QuPage::PageType QuPage::type() const
{
    return m_type;
}


QString QuPage::title() const
{
    return m_title;
}


bool QuPage::skip() const
{
    // You *can* skip a page that has "required input" missing; "skip" takes
    // higher priority.
    return m_skip;
}


bool QuPage::hasTag(const QString &tag) const
{
    return m_tags.contains(tag);
}


QPointer<QWidget> QuPage::widget(Questionnaire* questionnaire) const
{
    QPointer<QWidget> pagewidget(new BaseWidget());

    VBoxLayout* pagelayout = new VBoxLayout();

    pagewidget->setLayout(pagelayout);
    // Add widgets that we own directly
    for (QuElementPtr e : m_elements) {
        QPointer<QWidget> w = e->widget(questionnaire);
        pagelayout->addWidget(w);  // takes ownership
        w->setVisible(e->visible());  // only AFTER the widget is owned,
        // or this can create standalone windows!
    }
    // Propagate up events from *all* widgets, including those in grids etc.
    const QVector<QuElement*> elements = allElements();
    for (QuElement* e : elements) {
        connect(e, &QuElement::elementValueChanged,
                this, &QuPage::elementValueChanged,
                Qt::UniqueConnection);
    }
    // pagewidget->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Maximum);  // if we use QWidget
    // pagewidget->setObjectName(CssConst::DEBUG_YELLOW);
    return pagewidget;
}


QVector<QuElement*> QuPage::allElements() const
{
    QVector<QuElement*> elements;
    for (QuElementPtr e : m_elements) {
        elements.append(e.data());
        elements.append(e->subelementsWithChildrenFlattenedRaw());
    }
    return elements;
}


QVector<QuElement*> QuPage::elementsWithTag(const QString& tag)
{
    QVector<QuElement*> matching_elements;
    for (auto e : allElements()) {
        if (e->hasTag(tag)) {
            matching_elements.append(e);
        }
    }
    return matching_elements;
}


bool QuPage::missingInput() const
{
    const QVector<QuElement*> elements = allElements();
    for (QuElement* e : elements) {
        // Not this:
        /*
        if (e->missingInput()) {
            if (!e->visible()) {
                qWarning() << Q_FUNC_INFO << "TASK BUG: invisible widget "
                                             "blocking progress";
            }
            return true;
        }
        */

        // Instead, to make things considerably easier when writing tasks, use
        // the rule that invisible widgets cannot block progress.
        if (e->missingInput() && e->visible()) {
            return true;
        }
    }
    return false;
}


void QuPage::blockProgress(const bool block)
{
    m_progress_blocked = block;
}


bool QuPage::progressBlocked() const
{
    return m_progress_blocked;
}


void QuPage::closing()
{
    const QVector<QuElement*> elements = allElements();
    for (auto e : elements) {
        e->closing();
    }
}
