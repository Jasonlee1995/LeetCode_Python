class Solution:
    def minBitFlips(self, start, goal):
        return (start ^ goal).bit_count()