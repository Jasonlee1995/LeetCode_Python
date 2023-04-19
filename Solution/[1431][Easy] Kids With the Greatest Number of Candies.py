class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        threshold = max(candies) - extraCandies
        return [candy >= threshold for candy in candies]