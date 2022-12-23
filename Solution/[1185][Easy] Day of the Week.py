class Solution:
    def dayOfTheWeek(self, day, month, year):
        def check_leap(y):
            return (y % 400 == 0) or ((y % 100 != 0) and (y % 4 == 0))
            
        def count_days(start_year, target_year, target_month, target_day):
            months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            cnt = 0
            for y in range(start_year, target_year):
                cnt += sum(months) + check_leap(y)
            
            cnt += sum(months[:target_month-1])
            if target_month > 2:
                cnt += check_leap(target_year)

            cnt += target_day
            return cnt

        # solving date : 12 Nov 2022, Saturday
        days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        prior, target = (2022, 11, 12), (year, month, day)
        start_year = min(prior[0], target[0])
        
        cnt_prior, cnt_target = count_days(start_year, *prior), count_days(start_year, *target)
        return days[(cnt_target - cnt_prior) % 7]