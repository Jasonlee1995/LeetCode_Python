import collections

class Solution:
    def largestGoodInteger(self, num):
        cnt = collections.Counter(num)
        for n in sorted(cnt, reverse=True):
            if (cnt[n] >= 3) and (n*3 in num):
                return n*3
        return ""