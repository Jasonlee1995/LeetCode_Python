class Solution:
    def sortArrayByParity(self, nums):
        i, j = 0, len(nums)-1
        while i < j:
            ri, rj = nums[i] % 2, nums[j] % 2
            if ri > rj: nums[i], nums[j] = nums[j], nums[i]
            if ri == 0: i += 1
            if rj == 1: j -= 1
        return nums