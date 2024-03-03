class Solution:
    def canBeIncreasing(self, nums):
        idxs = []
        for idx in range(len(nums)-1):
            if nums[idx] >= nums[idx+1]:
                idxs.append(idx)

        if len(idxs) == 0:
            return True
        
        if len(idxs) == 1:
            idx = idxs[0]
            if (idx == 0) or (idx == len(nums)-2):
                return True
            if (nums[idx-1] < nums[idx+1]) or (nums[idx] < nums[idx+2]):
                return True
        
        return False