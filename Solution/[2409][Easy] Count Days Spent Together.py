class Solution:
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        def str2days(s):
            md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            mm, dd = s.split("-")
            mm, dd = int(mm), int(dd)
            return sum(md[:mm-1]) + dd
        
        aa, la = str2days(arriveAlice), str2days(leaveAlice)
        ab, lb = str2days(arriveBob), str2days(leaveBob)

        if   aa <= ab <= la <= lb:
            return la - ab + 1
        elif ab <= aa <= la <= lb:
            return la - aa + 1
        elif aa <= ab <= lb <= la:
            return lb - ab + 1
        elif ab <= aa <= lb <= la:
            return lb - aa + 1
        else:
            return 0

