class Solution:
    def findTheDifference(self, s, t):
        return chr(sum(map(ord, t)) - sum(map(ord, s)))
