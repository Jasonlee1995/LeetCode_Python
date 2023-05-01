class Solution:
    def isPrefixOfWord(self, sentence, searchWord):
        words = sentence.split()
        for idx, word in enumerate(words, start=1):
            if word.startswith(searchWord):
                return idx
        return -1