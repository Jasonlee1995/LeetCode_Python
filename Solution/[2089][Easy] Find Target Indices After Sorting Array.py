class Solution:
    def targetIndices(self, nums, target):
        nums.sort()
        return [idx for idx, num in enumerate(nums) if num == target]