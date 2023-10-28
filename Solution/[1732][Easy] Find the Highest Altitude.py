import itertools

class Solution:
    def largestAltitude(self, gain):
        return max(itertools.accumulate(gain, initial=0))