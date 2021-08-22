import collections


class Solution:
    def isAnagram(self, s, t):
        return collections.Counter(s) == collections.Counter(t)
