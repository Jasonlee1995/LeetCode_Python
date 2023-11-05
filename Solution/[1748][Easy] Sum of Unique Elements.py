import collections

class Solution:
    def sumOfUnique(self, nums):
        cnt = collections.Counter(nums)
        return sum(num for num in cnt if cnt[num] == 1)