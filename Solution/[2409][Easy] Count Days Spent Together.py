class Solution:
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        def str2days(s):
            md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            mm, dd = s.split("-")
            mm, dd = int(mm), int(dd)
            return sum(md[:mm-1]) + dd
        
        arrive = str2days(max(arriveAlice, arriveBob))
        leave  = str2days(min(leaveAlice,  leaveBob))
        return max(0, leave - arrive + 1)