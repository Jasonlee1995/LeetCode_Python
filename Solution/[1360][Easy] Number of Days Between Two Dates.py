class Solution:
    def daysBetweenDates(self, date1, date2):
        def isLeap(year):
            return (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0))

        def str2ymd(date):
            return list(map(int, date.split('-')))

        def countdays(ymd):
            year, month, day = ymd
            month2days = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            days = 0
            for y in range(1971, year):
                days += 365 + isLeap(y)
            for m in range(1, month):
                if m == 2: days += isLeap(year)
                days += month2days[m]
            days += day
            return days

        return abs(countdays(str2ymd(date1)) - countdays(str2ymd(date2)))