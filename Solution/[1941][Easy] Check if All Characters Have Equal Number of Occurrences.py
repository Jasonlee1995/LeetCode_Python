import collections

class Solution:
    def areOccurrencesEqual(self, s):
        return len(set(collections.Counter(s).values())) == 1