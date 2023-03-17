class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        num2idx = {}
        for idx, num in enumerate(sorted_nums):
            if num not in num2idx:
                num2idx[num] = idx

        return [num2idx[num] for num in nums]