import collections

class Solution:
    def intersection(self, nums):
        cnt = collections.Counter(nums[0])
        for idx in range(1, len(nums)):
            cnt += collections.Counter(nums[idx])
        return [num for num in sorted(cnt) if cnt[num] == len(nums)]