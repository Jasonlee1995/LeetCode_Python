class Solution:
    def findMiddleIndex(self, nums):
        leftSum, totalSum = 0, sum(nums)
        for idx, num in enumerate(nums):
            if 2 * leftSum == totalSum - num:
                return idx
            leftSum += num

        return -1