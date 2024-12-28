class Solution:
    def findSubarrays(self, nums):
        stack = [nums[idx] + nums[idx+1] for idx in range(len(nums)-1)]
        return len(stack) != len(set(stack))