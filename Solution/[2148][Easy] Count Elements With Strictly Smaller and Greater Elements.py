class Solution:
    def countElements(self, nums):
        n_min, n_max = min(nums), max(nums)
        return sum(1 for num in nums if num not in [n_min, n_max])