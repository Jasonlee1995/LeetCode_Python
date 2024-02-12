class Solution:
    def subsetXORSum(self, nums):
        orsum = 0
        for num in nums:
            orsum = orsum | num
        n = len(nums)
        return orsum * (2 ** (n-1))