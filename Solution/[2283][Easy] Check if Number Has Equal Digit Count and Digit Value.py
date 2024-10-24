import collections

class Solution:
    def digitCount(self, num):
        cnt = collections.Counter(num)
        for idx, n in enumerate(num):
            if cnt[str(idx)] != int(n):
                return False
        return True