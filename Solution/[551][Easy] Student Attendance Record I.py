class Solution:
    def checkRecord(self, s):
        return (s.count('LLL') == 0) and (s.count('A') < 2)
