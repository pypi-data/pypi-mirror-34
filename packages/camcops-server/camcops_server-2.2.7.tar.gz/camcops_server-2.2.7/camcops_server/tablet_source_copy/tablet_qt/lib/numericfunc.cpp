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

#include "numericfunc.h"
#include <QString>


namespace numeric {


// ============================================================================
// Overloaded functions to convert to an integer type
// ============================================================================

int strToNumber(const QString& str, const int type_dummy)
{
    Q_UNUSED(type_dummy);
    return str.toInt();
}


int localeStrToNumber(const QString& str, bool& ok,
                      const QLocale& locale, const int type_dummy)
{
    Q_UNUSED(type_dummy);
    return locale.toInt(str, &ok);
}


qlonglong strToNumber(const QString& str, const qlonglong type_dummy)
{
    Q_UNUSED(type_dummy);
    return str.toLongLong();
}


qlonglong localeStrToNumber(const QString& str, bool& ok,
                            const QLocale& locale, const qlonglong type_dummy)
{
    Q_UNUSED(type_dummy);
    return locale.toLongLong(str, &ok);
}


qulonglong strToNumber(const QString& str, const qulonglong type_dummy)
{
    Q_UNUSED(type_dummy);
    return str.toULongLong();
}


qulonglong localeStrToNumber(const QString& str, bool& ok,
                             const QLocale& locale,
                             const qulonglong type_dummy)
{
    Q_UNUSED(type_dummy);
    return locale.toULongLong(str, &ok);
}


// ============================================================================
// For double validation
// ============================================================================

int numDigitsDouble(const double number, const int max_dp)
{
    // Counts the number of digits in a floating-point number.
    // - ignores sign
    // - includes decimal point

    const QString formatted = QString::number(number, 'f', max_dp);
    const bool sign_present = number < 0;
    // Trim trailing zeros:
    int pos;
    for (pos = formatted.length() - 1; pos > 0; --pos) {
        if (formatted.at(pos) != '0') {
            break;
        }
    }
    int length = pos + 1;
    return sign_present ? length - 1 : length;
}


double firstDigitsDouble(const double number,
                         const int n_digits,
                         const int max_dp)
{
    // Returns the first n_digits of a floating point number, as a double.
    // - sign is ignored (can't compare numbers without dropping it)
    // - includes decimal point
    const QString formatted = QString::number(number, 'f', max_dp);
    const bool sign_present = number < 0;
    const QString left = formatted.left(sign_present ? n_digits + 1 : n_digits);
    const double result = left.toDouble();
#ifdef DEBUG_VALIDATOR
    qDebug() << Q_FUNC_INFO << "- formatted" << formatted
             << "n_digits" << n_digits
             << "left" << left
             << "result" << result;
#endif
    return result;
}


bool isValidStartToDouble(const double number,
                          const double bottom,
                          const double top)
{
    if (extendedDoubleMustBeLessThan(number, bottom, top)) {
#ifdef DEBUG_VALIDATOR
        qDebug() << Q_FUNC_INFO << number
                 << "when extended must be less than bottom value of"
                 << bottom << "=> fail";
#endif
        return false;
    }
    if (extendedDoubleMustExceed(number, bottom, top)) {
#ifdef DEBUG_VALIDATOR
        qDebug() << Q_FUNC_INFO << number
                 << "when extended must be more than top value of"
                 << top << "=> fail";
#endif
        return false;
    }
#ifdef DEBUG_VALIDATOR
    qDebug() << Q_FUNC_INFO << number << "is OK for bottom"
             << bottom << "top" << top;
#endif
    return true;
}


bool extendedDoubleMustExceed(const double number,
                              const double bottom,
                              const double top)
{
    if (number < 0 && top > 0) {
        return false;
    }
    if (number > 0 && top < 0) {
        return true;
    }
    const int nd_number = numDigitsDouble(number);
    QString str_number = QString("%1").arg(number);
    if (number > 0) {
        // Both positive. Extend with zeros, to length of top
        const int nd_top = numDigitsDouble(top);
        for (int i = 0; i < nd_top - nd_number; ++i) {
            str_number += "0";
            if (str_number.toDouble() <= top) {
                return false;
            }
        }
        return true;
    } else {
        // Both negative. Extend with nines.
        const int nd_bottom = numDigitsDouble(bottom);
        for (int i = 0; i < nd_bottom - nd_number; ++i) {
            str_number += "9";
            if (str_number.toDouble() <= top) {
                return false;
            }
        }
        return true;
    }
}


bool extendedDoubleMustBeLessThan(const double number,
                                  const double bottom,
                                  const double top)
{
    if (number < 0 && bottom > 0) {
        return true;
    }
    if (number > 0 && bottom < 0) {
        return false;
    }
    const int nd_number = numDigitsDouble(number);
    QString str_number = QString("%1").arg(number);
    if (number > 0) {
        // Both positive. Extend with nines, to length of top
        const int nd_top = numDigitsDouble(top);
        for (int i = 0; i < nd_top - nd_number; ++i) {
            str_number += "9";
            if (str_number.toDouble() >= bottom) {
                return false;
            }
        }
        return true;
    } else {
        // Both negative. Extend with zeros, to length of bottom
        const int nd_bottom = numDigitsDouble(bottom);
        for (int i = 0; i < nd_bottom - nd_number; ++i) {
            str_number += "0";
            if (str_number.toDouble() >= bottom) {
                return false;
            }
        }
        return true;
    }
}


}  // namespace numeric
