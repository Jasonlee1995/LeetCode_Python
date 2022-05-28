import collections, math


class Solution:
    def hasGroupsSizeX(self, deck):
        nums = set(collections.Counter(deck).values())
        m = min(nums)
        for num in nums:
            m = math.gcd(num, m)
            if m == 1: break
        return m >= 2