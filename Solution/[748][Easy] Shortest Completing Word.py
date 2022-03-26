import collections


class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        filtered = collections.Counter([letter.lower() for letter in licensePlate if letter.isalpha()])
        answer, size = None, None
        for word in words:
            if filtered - collections.Counter(word) == collections.Counter():
                if not size or size > len(word):
                    answer, size = word, len(word)
        return answer
