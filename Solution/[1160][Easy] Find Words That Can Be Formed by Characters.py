import collections


class Solution:
    def countCharacters(self, words, chars):
        answer = 0
        chars_count = collections.Counter(chars)
        for word in words:
            word_count = collections.Counter(word)
            if len(word_count - chars_count) == 0:
                answer += len(word)
        return answer