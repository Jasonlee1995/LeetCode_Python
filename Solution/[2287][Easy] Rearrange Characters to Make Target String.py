import collections

class Solution:
    def rearrangeCharacters(self, s, target):
        cnt_s = collections.Counter(s)
        cnt_t = collections.Counter(target)
        return min(cnt_s[abc] // cnt_t[abc] for abc in cnt_t)