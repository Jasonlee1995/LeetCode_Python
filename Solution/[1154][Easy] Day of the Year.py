class Solution:
    def dayOfYear(self, date):
        info = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year, month, day = map(int, date.split('-'))
        if (year % 400 == 0) or ((year % 100 != 0) and (year % 4) == 0):
            info[1] = 29
        
        return day + sum(info[:month-1])