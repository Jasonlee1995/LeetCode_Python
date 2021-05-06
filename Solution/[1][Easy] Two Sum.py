class Solution:
    def twoSum(self, nums, target):
        check = {}
        for idx, num in enumerate(nums):
            if target-num in check:
                return [check[target-num], idx]
            check[num] = idx
