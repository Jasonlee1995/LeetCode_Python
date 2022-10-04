class Solution:
    def largestSumAfterKNegations(self, nums, k):
        nums.sort()
        idx = 0
        while (idx < len(nums)) and (k > 0) and (nums[idx] < 0):
            nums[idx] *= -1
            k -= 1
            idx += 1
        if (k == 0) or (k % 2 == 0):
            return sum(nums)
        else:
            return sum(nums) - 2 * min(nums)