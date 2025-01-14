import collections

class Solution:
    def equalFrequency(self, word):
        cnt = collections.Counter(word)
        for k in set(word):
            cnt[k] -= 1
            if cnt[k] == 0: cnt.pop(k)
            if len(set(cnt.values())) == 1: return True
            cnt[k] = cnt.get(k, 0) + 1
        return False