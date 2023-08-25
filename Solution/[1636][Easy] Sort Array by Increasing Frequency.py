import collections


class Solution:
    def frequencySort(self, nums):
        counter = collections.Counter(nums)
        return sorted(nums, key=lambda x: (counter[x], -x))