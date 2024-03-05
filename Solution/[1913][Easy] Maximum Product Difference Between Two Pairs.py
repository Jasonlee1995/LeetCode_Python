class Solution:
    def maxProductDifference(self, nums):
        min1 = min2 = max(nums)
        max1 = max2 = 0
        for idx in range(len(nums)):
            if nums[idx] >= max1:
                max1, max2 = nums[idx], max1
            elif nums[idx] > max2:
                max2 = nums[idx]
            if nums[idx] <= min1:
                min1, min2 = nums[idx], min1
            elif nums[idx] < min2:
                min2 = nums[idx]
        return (max1 * max2) - (min1 * min2)