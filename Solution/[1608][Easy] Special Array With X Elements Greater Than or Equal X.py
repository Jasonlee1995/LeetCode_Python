class Solution:
    def specialArray(self, nums):
        nums.sort(reverse=True)
        idx = 0
        while (idx < len(nums)) and (idx < nums[idx]):
            idx += 1
        
        if (idx < len(nums)) and (idx == nums[idx]):
            return -1
        return idx