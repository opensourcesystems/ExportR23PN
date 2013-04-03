# -*- coding: utf-8 -*-
#############################################################################
##
## Copyright (C) 2006-2012 Chuk&Gek and Vista Software. All rights reserved.
## Copyright (C) 2012 SAMSON Group. All rights reserved.
##
#############################################################################
##
## Это программа является свободным программным обеспечением.
## Вы можете использовать, распространять и/или модифицировать её согласно
## условиям GNU GPL версии 3 или любой более поздней версии.
##
#############################################################################

import re
import datetime
from PyQt4 import QtGui
from PyQt4.QtCore import *


class smartDict:
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __len__(self):
        return len(self.__dict__)

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]

    def __iter__(self):
        return self.__dict__.__iter__()

    def __contain__(self, key):
        return key in self.__dict__

    def clear(self):
        self.__dict__.clear()

    def copy(self):
        return smartDict(self.__dict__)

    def get(self, key, default=None):
        return self.__dict__.get(key, default)

    def setdefault(self, key, default=None):
        return self.__dict__.setdefault(key, default)

    def update(self, d, **i):
        return self.__dict__.update(d, **i)

    def items(self):
        return self.__dict__.items()

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def iteritems(self):
        return self.__dict__.iteritems()

    def iterkeys(self):
        return self.__dict__.iterkeys()

    def itervalues(self):
        return self.__dict__.itervalues()


#############################################################################


def getVal(dict, key, default):
    return dict.get(key, default)

def getPref(dict, key, default):
    return dict.get(unicode(key).lower(), default)

def getPrefDate(dict, key, default):
    return forceDate(dict.get(unicode(key).lower(), default))

def getPrefTime(dict, key, default):
    return forceTime(dict.get(unicode(key).lower(), default))

def getPrefRef(dict, key, default):
    return forceRef(dict.get(unicode(key).lower(), default))

def getPrefBool(dict, key, default):
    return forceBool(dict.get(unicode(key).lower(), default))

def getPrefInt(dict, key, default):
    return forceInt(dict.get(unicode(key).lower(), default))

def getPrefString(dict, key, default):
    return forceString(dict.get(unicode(key).lower(), default))


def setPref(dict, key, value):
    dict[unicode(key).lower()] = value


def trim(s):
    return u' '.join(unicode(s).split())


def nameCase(s):
    r = u''
    up = True
    for c in s:
        if c.isalpha():
            if up:
                r += c.upper()
                up = False
            else:
                r += c.lower()
        else:
            up = True
            r += c
    return r


def isNameValid(name):
    return not re.search(r'''[0-9a-zA-Z`~!@#$%^&*_=+\\|{}[\];:'"<>?/]''', forceStringEx(name))


def splitDocSerial(serial):
    for c in '-=/_|':
        serial = serial.replace(c,' ')
    parts = trim(serial).partition(' ')
    return parts[0], parts[2]


def addDots(s):
    if s and not s.endswith('...'):
        return s + '...'
    else:
        return s


def addDotsBefore(s):
    if s and not s.startswith('...'):
        return '...' + s
    else:
        return s


def addDotsEx(s):
    if s:
        result = s
        if not s.startswith('...'): result = '...' + result
        if not s.endswith('...'):   result = result + '...'
        return result
    else:
        return s


def toVariant(v):
    if v is None:
        return QVariant()
    t = type(v)
    if t == QVariant:
        return v
    elif t == datetime.time:
        return QVariant(QTime(v))
    elif t == datetime.datetime:
        return QVariant(QDateTime(v))
    elif t == datetime.date:
        return QVariant(QDate(v))
    else:
        return QVariant(v)


def variantEq(value1, value2):
    return (value1.isNull() and value2.isNull()) or (value1 == value2)


#############################################################################


def forceBool(val):
    if isinstance(val, QVariant):
        return val.toBool()
    return bool(val)


def forceDate(val):
    if isinstance(val, QVariant):
        return val.toDate()
    if isinstance(val, QDate):
        return val
    if isinstance(val, QDateTime):
        return val.date()
    if val is None:
        return QDate()
    return QDate(val)


def forceTime(val):
    if isinstance(val, QVariant):
        return val.toTime()
    if isinstance(val, QTime):
        return val
    if isinstance(val, QDateTime):
        return val.time()
    if val is None:
        return QTime()
    return QTime(val)


def forceDateTime(val):
    if isinstance(val, QVariant):
        return val.toDateTime()
    if isinstance(val, QDateTime):
        return val
    if isinstance(val, QDate):
        return QDateTime(val)
    if isinstance(val, QTime):
        return QDateTime(QDate(), val)
    if val is None:
        return QDateTime()
    return QDateTime(val)


def forceInt(val):
    if isinstance(val, QVariant):
        return val.toInt()[0]
    elif val is None:
        return 0
    return int(val)


def forceLong(val):
    if isinstance(val, QVariant):
        return val.toLongLong()[0]
    elif val is None:
        return 0L
    return long(val)


def forceRef(val):
    if isinstance(val, QVariant):
        if val.isNull():
            val = None
        else:
            val = val.toInt()[0]
            if val == 0:
                val = None
    return val


def forceString(val):
    if isinstance(val, QVariant):
        valType = val.type()
        if  valType == QVariant.Date:
            return formatDate(val.toDate())
        elif valType == QVariant.DateTime:
            return formatDateTime(val.toDateTime())
        elif valType == QVariant.Time:
            return formatTime(val.toTime())
        else:
            val = val.toString()
    if isinstance(val, QDate):
        return formatDate(val)
    if isinstance(val, QDateTime):
        return formatDateTime(val)
    if isinstance(val, QTime):
        return formatTime(val)
    if val is None:
        return u''
    return unicode(val)


def forceStringEx(val):
    return trim(forceString(val))


def forceDouble(val):
    if isinstance(val, QVariant):
        return val.toDouble()[0]
    else:
        return float(val)


def formatBool(val):
    if forceBool(val):
        return u'да'
    else:
        return u'нет'


def pyDate(date):
    if date and date.isValid():
        return date.toPyDate()
    else:
        return None


#############################################################################


def formatDate(val):
    if isinstance(val, QVariant):
        val = val.toDate()
    return unicode(val.toString('dd.MM.yyyy'))


def formatTime(val):
    if isinstance(val, QVariant):
        val = val.toDate()
    return unicode(val.toString('H:mm'))


def formatDateTime(val):
    if isinstance(val, QVariant):
        val = val.toDateTime()
    return unicode(val.toString('dd.MM.yyyy H:mm'))


def formatNameInt(lastName, firstName, patrName):
    return trim(lastName+' '+firstName+' '+patrName)


def formatName(lastName, firstName, patrName):
    lastName  = nameCase(forceStringEx(lastName))
    firstName = nameCase(forceStringEx(firstName))
    patrName  = nameCase(forceStringEx(patrName))
    return formatNameInt(lastName, firstName, patrName)


def formatShortNameInt(lastName, firstName, patrName):
    return trim(lastName + ' ' +((firstName[:1]+'.') if firstName else '') + ((patrName[:1]+'.') if patrName else ''))


def formatShortName(lastName, firstName, patrName):
    lastName  = nameCase(forceStringEx(lastName))
    firstName = nameCase(forceStringEx(firstName))
    patrName  = nameCase(forceStringEx(patrName))
    return formatShortNameInt(lastName, firstName, patrName)


def formatSex(sex):
    sex = forceInt(sex)
    if sex == 1:
        return u'М'
    elif sex == 2:
        return u'Ж'
    else:
        return u''


def formatSNILS(SNILS):
    if SNILS:
        s = forceString(SNILS)+' '*14
        return s[0:3]+'-'+s[3:6]+'-'+s[6:9]+' '+s[9:11]
    else:
        return u''


def unformatSNILS(SNILS):
    return forceString(SNILS).replace('-', '').replace(' ', '')


def calcSNILSCheckCode(SNILS):
    result = 0
    for i in xrange(9):
        result += (9-i)*int(SNILS[i])
    result = result % 101
    if result == 100:
        result = 0
    return '%02.2d' % result


def checkSNILS(SNILS):
    raw = unformatSNILS(SNILS)
    if len(raw) == 11:
        return raw[:9]<='001001998' or raw[-2:] == calcSNILSCheckCode(raw)
    return False


def fixSNILS(SNILS):
    raw = unformatSNILS(SNILS)
    return (raw+'0'*11)[:9] + calcSNILSCheckCode(raw)


def agreeNumberAndWord(num, words):
    u"""
        Согласовать число и слово:
        num - число, слово = (один, два, много)
        agreeNumberAndWord(12, (u'год', u'года', u'лет'))
    """
    if num<0: num = -num
    if (num/10)%10 != 1:
        if num%10 == 1:
            return words[0]
        elif 1 < num%10 < 5:
            return words[1]
    return words[-1]


def formatNum(num, words):
    return u'%d %s' % (num, agreeNumberAndWord(num,words))


def formatNum1(num, words):
    if num == 1:
        return agreeNumberAndWord(num,words)
    else:
        return u'%d %s' % (num, agreeNumberAndWord(num,words))


def formatYears(years):
    return '%d %s' % (years, agreeNumberAndWord(years, (u'год', u'года', u'лет')))


def formatMonths(months):
    return '%d %s' % (months, agreeNumberAndWord(months, (u'месяц', u'месяца', u'месяцев')))


def formatWeeks(weeks):
    return '%d %s' % (weeks, agreeNumberAndWord(weeks, (u'неделя', u'недели', u'недель')))


def formatDays(days):
    return '%d %s' % (days, agreeNumberAndWord(days, (u'день', u'дня', u'дней')))


def formatYearsMonths(years, months):
    if years == 0:
        return formatMonths(months)
    elif months == 0:
        return formatYears(years)
    else:
        return formatYears(years) + ' ' + formatMonths(months)


def formatMonthsWeeks(months, weeks):
    if  months == 0:
        return formatWeeks(weeks)
    elif weeks == 0:
        return formatMonths(months)
    else:
        return formatMonths(months) + ' ' + formatWeeks(weeks)


def formatRecordsCountInt(count):
    return '%d %s' % (count, agreeNumberAndWord(count, (u'запись', u'записи', u'записей')))


def formatRecordsCount(count):
    if count:
        return u'в списке '+formatRecordsCountInt(count)
    else:
        return u'список пуст'


def formatRecordsCount2(count, totalCount):
    if count and totalCount and count<totalCount:
        return formatRecordsCount(totalCount)+ u', показаны первые '+formatRecordsCountInt(count)
    else:
        return formatRecordsCount(count)


def formatList(list):
    if len(list)>2:
        return u' и '.join([', '.join(list[:-1]), list[-1]])
    else:
        return u' и '.join(list)


def splitText(text, widths):
    result = []
    if not text:
        return result

    width = widths[0]

    lines = text.splitlines()
    count = 0

    for line in lines:
        p = 0
        l = len(line)
        while p<l:
            while line[p:p+1].isspace():
                p += 1
            s = p + width
            if s>=l:
                breakpos = s
            else:
                breakpos = line.rfind(' ', p, s+1)
            if breakpos<0:
                breakpos = max([line.rfind(sep, p, s) for sep in '-,.;:!?)]}\\|/'])
                if breakpos>= 0:
                  breakpos+=1
            if breakpos<0:
                breakpos = s
            result.append(line[p:breakpos])
            p = breakpos
            count += 1
            width = widths[count if count<len(widths) else -1]
    return result


def foldText(text, widths):
    return '\n'.join(splitText(text, widths))


#############################################################################


def calcAgeInDays(birthDay, today):
    assert isinstance(birthDay, QDate)
    assert isinstance(today, QDate)
    return birthDay.daysTo(today)


def calcAgeInWeeks(birthDay, today):
    return calcAgeInDays(birthDay, today)/7


def calcAgeInMonths(birthDay, today):
    assert isinstance(birthDay, QDate)
    assert isinstance(today, QDate)

    bYear  = birthDay.year()
    bMonth = birthDay.month()
    bDay   = birthDay.day()

    tYear  = today.year()
    tMonth = today.month()
    tDay   = today.day()

    result = (tYear-bYear)*12+(tMonth-bMonth)
    if bDay > tDay:
        result -= 1
    return result


def calcAgeInYears(birthDay, today):
    assert isinstance(birthDay, QDate)
    assert isinstance(today, QDate)

    bYear  = birthDay.year()
    bMonth = birthDay.month()
    bDay   = birthDay.day()

    tYear  = today.year()
    tMonth = today.month()
    tDay   = today.day()

    result = tYear-bYear
    if bMonth>tMonth or (bMonth == tMonth and bDay > tDay):
        result -= 1
    return result


def calcAgeTuple(birthDay, today):
    if not today or today.isNull():
        today = QDate.currentDate()
    elif isinstance(today, QDateTime):
        today = today.date()
    d = calcAgeInDays(birthDay, today)
    if d>=0:
        return (d,
                d/7,
                calcAgeInMonths(birthDay, today),
                calcAgeInYears(birthDay, today)
               )
    else:
        return None


def formatAgeTuple(ageTuple, bd, td):
    if not ageTuple:
        return u'ещё не родился'
    (days, weeks, months, years) = ageTuple
    if years>=7:
        return formatYears(years)
    elif years>=1:
        return formatYearsMonths(years, months-12*years)
    elif months>=1:
        if not td:
            td = QDate.currentDate()
        return formatMonthsWeeks(months, bd.addMonths(months).daysTo(td)/7)
    else:
        return formatDays(days)


def calcAge(birthDay, today=None):
    bd = forceDate(birthDay)
    td = forceDate(today) if today else QDate.currentDate()
    ageTuple = calcAgeTuple(bd, td)
    return formatAgeTuple(ageTuple, bd, td)


def firstWeekDay(date):
#    return date.addDays(-(date.dayOfWeek()-1))
    return date.addDays(1-date.dayOfWeek())


def lastWeekDay(date):
#    return firstWeekDay.addDays(6)
    return date.addDays(7-date.dayOfWeek())


def firstMonthDay(date):
    return QDate(date.year(), date.month(), 1)


def lastMonthDay(date):
    return firstMonthDay(date).addMonths(1).addDays(-1)


def firstQuarterDay(date):
    month = ((date.month()-1)/3)*3+1
    return QDate(date.year(), month, 1)


def lastQuarterDay(date):
    return firstQuarterDay(date).addMonths(3).addDays(-1)


def firstHalfYearDay(date):
    month = 1 if date.month() < 7 else 7
    return QDate(date.year(), month, 1)


def lastHalfYearDay(date):
    return firstHalfYearDay(date).addMonths(6).addDays(-1)


def firstYearDay(date):
    return QDate(date.year(), 1, 1)


def lastYearDay(date):
    return QDate(date.year(), 12, 31)


#############################################################################


# описание рабочих дней для разных вариантов работы
wpFiveDays = (0, 1, 2, 3, 4, 5, 5, 5) # пятидневка
wpSixDays  = (0, 1, 2, 3, 4, 5, 6, 6) # шестидневка
wpSevenDays= (0, 1, 2, 3, 4, 5, 6, 7) # полная неделя

def _determineMondayAndWorkDaysCount(date, weekProfile):
    # date: QDate
    # weekProfile: список или кортеж из 8 значений, нулевое - нуль,
    # weekProfile[doy] - количество предшествующих рабочих дней включая день doy
    # соглажение Qt: понедельник - doy == 1, воскресение - doy == 7
    doy = date.dayOfWeek()
    monday = date.addDays(Qt.Monday-doy)
    workDaysCount = weekProfile[doy]
    return monday, workDaysCount, workDaysCount == weekProfile[doy-1]

def countWorkDays(startDate, stopDate, weekProfile):
    # определение количества рабочих дней в заданном отрезке дат
    # учитывается и начальная и конечная дата
    # weekProfile: список или кортеж из 8 значений, нулевое - нуль,
    # weekProfile[doy] - количество  предшествующих рабочих дней включая день doy
    # соглажение Qt: понедельник - doy == 1, воскресение - doy == 7
    # возможно, что необходимо доделать для работы с праздничными днями
    if weekProfile is wpSevenDays:
        return startDate.daysTo(stopDate)+1
    else:
        startMonday, startWDC, startIsRed = _determineMondayAndWorkDaysCount(startDate, weekProfile)
        stopMonday, stopWDC, stopIsRed = _determineMondayAndWorkDaysCount(stopDate, weekProfile)
        return startMonday.daysTo(stopMonday)*weekProfile[-1]//7+stopWDC-startWDC+(0 if startIsRed else 1)


def addWorkDays(startDate, duration, weekProfile):
    # добавление к некоторой дате некоторого периода в рабочих днях
    # длительность с учётом начальной и конечной даты
    # weekProfile: список или кортеж из 8 значений, нулевое - нуль,
    # weekProfile[doy] - количество рабочих дней включая день doy
    # соглажение Qt: понедельник - doy == 1, воскресение - doy == 7
    # возможно, что необходимо доделать для работы с праздничными днями
    if duration>1:
        if weekProfile is wpSevenDays:
            return startDate.addDays(duration-1)
        elif duration>=1:
            correctStartDate = QDate(startDate)
            doy = correctStartDate.dayOfWeek()
            while weekProfile[doy] == weekProfile[doy-1]:
                correctStartDate = correctStartDate.addDays(1)
                doy = doy+1 if doy<7 else 1
            week, days = divmod(duration-1, weekProfile[-1])
            stopDate = correctStartDate.addDays(week*7)
            while days:
                stopDate = stopDate.addDays(1)
                doy = doy%7+1
                if weekProfile[doy] != weekProfile[doy-1]:
                    days -= 1
            return stopDate
    else:
        return startDate


def getNextWorkDay(date, weekProfile):
    doy = date.dayOfWeek()
    offset = 0
    while offset<7:
        offset += 1
        doy = doy%7 + 1
        if weekProfile[doy] != weekProfile[doy-1]:
            return date.addDays(offset)
    return date # fall-back: неверный профиль недели


monthName =   ['', u'январь', u'февраль', u'март', u'апрель', u'май', u'июнь', u'июль', u'август', u'сентябрь', u'октябрь', u'ноябрь', u'декабрь']
monthNameGC = ['', u'января', u'февраля', u'марта', u'апреля', u'мая', u'июня', u'июля', u'августа', u'сентября', u'октября', u'ноября', u'декабря']


#############################################################################


def setBits(val, mask, bits):
    return ( val & ~mask ) | ( bits & mask )


def checkBits(val, mask, bits):
    return ( val & mask ) == ( bits & mask )


#############################################################################

def sorry(widget=None):
    widget = widget or QtGui.qApp.focusWidget() or QtGui.qApp.activeWindow() or QtGui.qApp.mainWindow
    QtGui.QMessageBox.information(widget,
                                u'не реализовано',
                                u'к сожалению не реализовано :(',
                                QtGui.QMessageBox.Ok,
                                QtGui.QMessageBox.Ok
                                )


def oops(widget=None):
    widget = widget or QtGui.qApp.focusWidget() or QtGui.qApp.activeWindow() or QtGui.qApp.mainWindow
    QtGui.QMessageBox.information(widget,
                                u'ой',
                                u'косяк, однако! :\'(',
                                QtGui.QMessageBox.Ok,
                                QtGui.QMessageBox.Ok
                                )


def get_date(d):
    d=forceDate(d)
    if d and 1800<=d.year()<=2200:
        return d.toPyDate()
    else:
        return None


def getInfisCodes(KLADRCode, KLADRStreetCode, house, corpus):
    db = QtGui.qApp.db
    area = ''
    region = ''
    npunkt = ''
    street = '*'
    streettype = ''
    npunkt=forceString(db.translate('kladr.KLADR', 'CODE', KLADRCode, 'NAME'))
    if KLADRCode.startswith('78'):
        OCATO=forceString(db.translate('kladr.STREET', 'CODE', KLADRStreetCode, 'OCATD'))
        if KLADRStreetCode and not OCATO:
            firstPart = house.split('/')[0]
            if re.match('^\d+$', firstPart):
                intHouse = int(firstPart)
            else:
                intHouse = None
            table = db.table('kladr.DOMA')
            cond=table['CODE'].like(KLADRStreetCode[:-2]+'%')
            list = db.getRecordList(table, 'CODE,NAME,KORP,OCATD', where=cond)
            for record in list:
                NAME=forceString(record.value('NAME'))
                KORP=forceString(record.value('KORP'))
                if checkHouse(NAME, KORP, house, intHouse, corpus):
                    OCATO = forceString(record.value('OCATD'))
                    break
        if OCATO:
            area = forceString(db.translate('kladr.OKATO', 'CODE', OCATO[:5], 'infis'))
        if KLADRCode!='7800000000000':
            region = forceString(db.translate(
                'kladr.KLADR', 'CODE', KLADRStreetCode[:-6]+'00', 'infis'))
            if region == u'СПб':
                region = area
        else:
            region = area
        street=forceString(db.translate('kladr.STREET', 'CODE', KLADRStreetCode, 'infis'))
        SOCR=forceString(db.translate('kladr.STREET', 'CODE', KLADRStreetCode, 'SOCR'))
        streettype=forceString(db.translate('kladr.SOCRBASE', 'SCNAME', SOCR, 'infisCODE'))
    elif KLADRCode.startswith('47'):
        KLADRArea   = KLADRCode[:2]+'0'*11
        KLADRRegion = KLADRCode[:5]+'0'*8
        area = forceString(db.translate('kladr.KLADR', 'CODE', KLADRArea, 'infis'))
        if KLADRArea != KLADRRegion:
            region = forceString(db.translate('kladr.KLADR', 'CODE', KLADRRegion, 'infis'))
        else:
            region = area
    else:
        KLADRArea   = KLADRCode[:2]+'0'*11
        area = forceString(db.translate('kladr.KLADR', 'CODE', KLADRArea, 'infis'))
        table = db.table('kladr.KLADR')
        region = area
        code = KLADRCode
        SOCR=forceString(db.translate('kladr.STREET', 'CODE', KLADRStreetCode, 'SOCR'))
        streettype=forceString(db.translate('kladr.SOCRBASE', 'SCNAME', SOCR, 'infisCODE'))
        while True:
            record = db.getRecordEx(table, 'parent, infis', table['CODE'].eq(code))
            if record:
                parent = forceString(record.value(0))
                infis  = forceString(record.value(1))
                if len(parent) <= 3 and infis:
                    region = infis
                    break
                else:
                    code = parent+'0'*(13-len(parent))
            else:
                break
    return area, region, npunkt, street, streettype


def checkHouse(rHouse, rCorpus, house, intHouse, corpus):
    for range in rHouse.split(','):
        if intHouse:
            simple = re.match('^(\d+)-(\d+)$', range)
            if simple:
                if int(simple.group(1)) <= intHouse <= int(simple.group(2)):
                    return True
                else:
                    continue
            if intHouse%2 == 0:
                even = re.match(u'^Ч\((\d+)-(\d+)\)$', range)
                if even:
                    if int(even.group(1)) <= intHouse <= int(even.group(2)):
                        return True
                    else:
                        continue
            else:
                odd = re.match(u'^Н\((\d+)-(\d+)\)$', range)
                if odd:
                    if int(odd.group(1)) <= intHouse <= int(odd.group(2)):
                        return True
                    else:
                        continue
        if house == range:
            return True
    return False


def copyFields(newRecord, record):
    for i in xrange(newRecord.count()):
        newRecord.setValue(i, record.value(newRecord.fieldName(i)))


def quote(str, sep='\''):
    magicChars = { '\\' : '\\\\',
                   sep  : '\\'+sep,
#                   '\n' : '\\n',
#                   '\r' : '\\r',
#                   '\0' : '\x00'
                 }
    res = ''
    for c in str:
        res += magicChars.get(c, c)
    return sep + res + sep


def MKBwithoutSubclassification(mkb):
    mkb = (mkb[:5]).strip()
    if mkb.endswith('.'):
        mkb = mkb[:-1]
    return mkb


def getActionTypeIdListByFlatCode(flatCode):
    db = QtGui.qApp.db
    tableActionType = db.table('ActionType')
    cond =[tableActionType['flatCode'].like(flatCode),
           tableActionType['deleted'].eq(0)
          ]
    return db.getIdList(tableActionType, 'id', cond)


def getMKB():
    return '''(SELECT Diagnosis.MKB
FROM Diagnosis INNER JOIN Diagnostic ON Diagnostic.diagnosis_id=Diagnosis.id
INNER JOIN rbDiagnosisType ON Diagnostic.diagnosisType_id=rbDiagnosisType.id
WHERE Diagnostic.event_id = Event.id AND Diagnosis.deleted = 0 AND Diagnostic.deleted = 0
AND (rbDiagnosisType.code = '1'
OR (rbDiagnosisType.code = '2' AND Diagnostic.person_id = Event.execPerson_id
AND (NOT EXISTS (SELECT DC.id FROM Diagnostic AS DC
INNER JOIN rbDiagnosisType AS DT ON DT.id = DC.diagnosisType_id WHERE DT.code = '1'
AND DC.event_id = Event.id
LIMIT 1))))) AS MKB'''


def getDataOSHB():
    return '''(SELECT CONCAT_WS('  ', OSHB.code, OSHB.name, IF(OSHB.sex=1, \'%s\', IF(OSHB.sex=2, \'%s\', ' ')))
FROM ActionPropertyType AS APT
INNER JOIN ActionProperty AS AP ON AP.type_id=APT.id
INNER JOIN ActionProperty_HospitalBed AS APHB ON APHB.id=AP.id
INNER JOIN OrgStructure_HospitalBed AS OSHB ON OSHB.id=APHB.value
WHERE APT.actionType_id=Action.actionType_id AND AP.action_id=Action.id AND AP.deleted=0 AND APT.deleted=0 AND APT.typeName LIKE 'HospitalBed') AS bedCodeName'''%(forceString(u''' /М'''), forceString(u''' /Ж'''))


def getAgeRangeCond(ageFor, ageTo):
    return '''(Action.begDate >= ADDDATE(Client.birthDate, INTERVAL %d YEAR))
           AND (Action.begDate < ADDDATE(Client.birthDate, INTERVAL %d YEAR))''' % (ageFor, ageTo+1)


def getKladrClientRural():
    return u'''EXISTS(SELECT kladr.KLADR.OCATD
    FROM ClientAddress
    INNER JOIN Address ON ClientAddress.address_id = Address.id
    INNER JOIN AddressHouse ON Address.house_id = AddressHouse.id
    INNER JOIN kladr.KLADR ON kladr.KLADR.CODE = AddressHouse.KLADRCode
    WHERE Client.id IS NOT NULL AND ClientAddress.client_id = Client.id AND (((SUBSTRING(kladr.KLADR.OCATD,3,1) IN (1, 2, 4)) AND SUBSTRING(kladr.KLADR.OCATD,6,1) = 8) OR ((SUBSTRING(kladr.KLADR.OCATD,3,1) NOT IN (1, 2, 4))
    AND SUBSTRING(kladr.KLADR.OCATD,6,1) = 9)))'''
