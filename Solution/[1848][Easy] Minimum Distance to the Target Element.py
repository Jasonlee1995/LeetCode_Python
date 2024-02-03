class Solution:
    def getMinDistance(self, nums, target, start):
        return min(abs(idx-start) for idx, num in enumerate(nums) if num == target)