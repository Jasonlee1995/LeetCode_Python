class Solution:
    def moveZeroes(self, nums):
        zero_idx = 0
        for idx, num in enumerate(nums):
            if num != 0:
                nums[zero_idx], nums[idx] = nums[idx], nums[zero_idx]
                zero_idx += 1
