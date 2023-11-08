class Solution:
    def check(self, nums):
        return sum(a > b for a,b in zip(nums, nums[1:] + nums[:1])) <= 1