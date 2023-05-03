import collections


class Solution:
    def canBeEqual(self, target, arr):
        return collections.Counter(target) == collections.Counter(arr)