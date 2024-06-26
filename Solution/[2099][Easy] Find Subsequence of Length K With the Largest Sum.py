class Solution:
    def maxSubsequence(self, nums, k):
        nums_with_idx = [(idx, num) for idx, num in enumerate(nums)]
        nums_with_kidx = sorted(nums_with_idx, key=lambda x: x[-1])[-k:]
        nums_with_kidx = sorted(nums_with_kidx, key=lambda x: x[0])
        return [num for _, num in nums_with_kidx]