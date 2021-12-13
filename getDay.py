from datetime import timedelta, date


def get_day_of_day(n=0):
    '''
    if n>=0,date is larger than today
    if n<0,date is less than today
    date format = "YYYY-MM-DD"
    '''

    if (n < 0):
        n = abs(n)
        return date.today() - timedelta(days=n)
    else:
        return date.today() + timedelta(days=n)


def getDateStr(day):
    if day == date.today():
        dateStr = day.strftime("%Y年%m月%d日(今天)")
    elif day == get_day_of_day(1):
        dateStr = day.strftime("%Y年%m月%d日(明天)")
    elif day == get_day_of_day(2):
        dateStr = day.strftime("%Y年%m月%d日(后天)")
    else:
        week = int(day.strftime("%w"))
        weeks = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
        dateStr = day.strftime("%Y年%m月%d日(" + weeks[week - 1] + ")")

    return dateStr


def main():
    day = get_day_of_day(1)
    print(day)
    print(getDateStr(day))


if __name__ == "__main__":
    main()
