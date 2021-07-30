class Solution:
    def majorityElement(self, nums):
        val, freq = 0, 0
        for num in nums:
            if freq == 0: val, freq = num, 1
            elif val == num: freq += 1
            else: freq -= 1
        return val
