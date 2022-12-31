import collections


class Solution:
    def uniqueOccurrences(self, arr):
        c = collections.Counter(arr)
        return len(c) == len(set(c.values()))