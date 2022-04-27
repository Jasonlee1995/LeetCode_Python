import collections


class Solution:
    def uncommonFromSentences(self, s1, s2):
        cnt = collections.Counter(s1.split()) + collections.Counter(s2.split())
        answer = [word for word in cnt if cnt[word] == 1]
        return answer
