import collections


class Solution:
    def maxNumberOfBalloons(self, text):
        text_cnt = collections.Counter(text)
        balloon_cnt = collections.Counter('balloon')
        return min(text_cnt[t] // balloon_cnt[t] for t in balloon_cnt)