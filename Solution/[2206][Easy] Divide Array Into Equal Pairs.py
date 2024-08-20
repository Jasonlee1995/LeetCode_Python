import collections

class Solution:
    def divideArray(self, nums):
        freq = collections.Counter(nums)
        for num in freq:
            if freq[num] % 2 == 1:
                return False
        return True