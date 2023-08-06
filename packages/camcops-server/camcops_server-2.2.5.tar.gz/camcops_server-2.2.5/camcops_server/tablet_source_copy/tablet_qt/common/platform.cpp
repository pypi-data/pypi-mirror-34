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

#include "platform.h"
#include <QtGlobal>

namespace platform {

#ifdef Q_OS_ANDROID
const bool PLATFORM_ANDROID = true;
#else
const bool PLATFORM_ANDROID = false;
#endif

#ifdef Q_OS_IOS
const bool PLATFORM_IOS = true;
#else
const bool PLATFORM_IOS = false;
#endif

#ifdef Q_OS_LINUX
const bool PLATFORM_LINUX = true;
#else
const bool PLATFORM_LINUX = false;
#endif

#ifdef Q_OS_WIN
const bool PLATFORM_WINDOWS = true;
#else
const bool PLATFORM_WINDOWS = false;
#endif

#if defined(Q_OS_ANDROID) || defined(Q_OS_IOS)
const bool PLATFORM_TABLET = true;
#else
const bool PLATFORM_TABLET = false;
#endif

}  // namespace platform
