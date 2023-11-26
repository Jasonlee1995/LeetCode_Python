class Solution:
    def checkOnesSegment(self, s):
        return s.count('10') + s.count('01') <= 1