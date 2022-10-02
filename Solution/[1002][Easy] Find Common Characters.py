import collections


class Solution:
    def commonChars(self, words):
        answer = collections.Counter(words[0])
        for i in range(1, len(words)):
            answer &= collections.Counter(words[i])
        return answer.elements()