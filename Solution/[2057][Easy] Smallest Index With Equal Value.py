class Solution:
    def smallestEqual(self, nums):
        for idx, num in enumerate(nums):
            if idx % 10 == num:
                return idx
        return -1