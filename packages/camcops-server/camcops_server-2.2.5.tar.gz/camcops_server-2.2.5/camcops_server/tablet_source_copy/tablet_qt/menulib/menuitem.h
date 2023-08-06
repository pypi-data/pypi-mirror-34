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

#include <functional>  // for std::function
#include <QCoreApplication>  // for Q_DECLARE_TR_FUNCTIONS
#include <QSharedPointer>
#include <QString>
#include "common/aliases_camcops.h"
#include "menulib/choosepatientmenuitem.h"  // many menus will want this
#include "menulib/menuproxy.h"
#include "menulib/htmlmenuitem.h"  // many menus will want this
#include "menulib/taskmenuitem.h"  // many menus will want this
#include "menulib/urlmenuitem.h"

class CamcopsApp;
class MenuWindow;
class OpenableWidget;
class QWidget;


class MenuItem
{
    Q_DECLARE_TR_FUNCTIONS(MenuItem)

public:
    using ActionFunction = std::function<void()>;
    using OpenableWidgetMaker = std::function<OpenableWidget*(CamcopsApp&)>;
    // http://stackoverflow.com/questions/14189440

public:
    MenuItem();
    MenuItem(const QString& title);  // for dummy use
    MenuItem(const QString& title, const ActionFunction& func,
             const QString& icon = "", const QString& subtitle = "");
    MenuItem(const QString& title, const OpenableWidgetMaker& func,
             const QString& icon = "", const QString& subtitle = "");
    MenuItem(MenuProxyPtr p_menuproxy, CamcopsApp& app);
    MenuItem(const ChoosePatientMenuItem& choose_patient, CamcopsApp& app);
    MenuItem(const TaskMenuItem& taskmenuitem, CamcopsApp& app);
    MenuItem(const QString& title, const HtmlMenuItem& htmlmenuitem,
             const QString& icon = "", const QString& subtitle = "");
    MenuItem(const QString& title, const UrlMenuItem& urlmenuitem,
             const QString& icon = "", const QString& subtitle = "");
    MenuItem(TaskPtr p_task, bool task_shows_taskname = true,
             bool task_shows_patient = false);
    // We don't have one for a Questionnaire or other generic OpenableWidget;
    // we don't want to have to create them all just to creat the menu.
    // Use a function instead, which can create the OpenableWidget (and open
    // it) as required.
    MenuItem(PatientPtr p_patient);

    QString title() const;
    TaskPtr task() const;
    PatientPtr patient() const;

    // https://en.wikipedia.org/wiki/Method_chaining
    MenuItem& setImplemented(bool implemented);
    MenuItem& setLabelOnly(bool label_only = true);
    MenuItem& setNeedsPrivilege(bool needs_privilege = true);
    MenuItem& setNotIfLocked(bool not_if_locked = true);
    MenuItem& setUnsupported(bool unsupported = true);

    QWidget* rowWidget(CamcopsApp& app) const;
    void act(CamcopsApp& app) const;
    void showHtml(const QString& filename) const;
    bool isImplemented() const;

    QString info() const;

protected:
    QString m_title;
    QString m_subtitle;
    QString m_icon;
    bool m_arrow_on_right;
    bool m_chain;
    bool m_copyright_details_pending;
    // bool m_crippled;
    bool m_implemented;
    bool m_label_only;
    bool m_needs_privilege;
    bool m_not_if_locked;
    bool m_task_shows_taskname;
    bool m_task_shows_patient;
    bool m_unsupported;
    ActionFunction m_func;
    OpenableWidgetMaker m_openable_widget_maker;
    MenuProxyPtr m_p_menuproxy;
    QString m_task_tablename;
    TaskPtr m_p_task;
    PatientPtr m_p_patient;
    HtmlMenuItem m_html_item;
    UrlMenuItem m_url_item;
//    SOMETHING m_event; // ***
//    SOMETHING m_chainList; // ***

private:
    void setDefaults();

public:
    friend QDebug operator<<(QDebug debug, const MenuItem& m);
    friend QDebug operator<<(QDebug debug, const MenuItem* m);
};


// ============================================================================
// Convenience macros
// ============================================================================

#define MAKE_MENU_MENU_ITEM(MenuClass, app) \
    MenuItem(MenuProxyPtr(new MenuProxy<MenuClass>), app)
#define MAKE_TASK_MENU_ITEM(tablename, app) \
    MenuItem(TaskMenuItem(tablename), app)
#define MAKE_CHANGE_PATIENT(app) \
    MenuItem(ChoosePatientMenuItem(), app).setNotIfLocked()


// ============================================================================
// The following classes exist just for CSS.
// ============================================================================

// This works, but using setObjectName and #selector is simpler!
/*
class MenuItemTitle : public QLabel
{
    Q_OBJECT
public:
    MenuItemTitle(QWidget* parent = nullptr, Qt::WindowFlags f = 0) :
        QLabel(parent, f)
    {}
    MenuItemTitle(const QString& text, QWidget* parent = nullptr,
                  Qt::WindowFlags f = 0) :
        QLabel(text, parent, f)
    {}
    virtual ~MenuItemTitle() {}
};
*/
