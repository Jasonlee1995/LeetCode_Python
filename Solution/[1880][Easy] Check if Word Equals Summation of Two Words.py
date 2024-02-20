class Solution:
    def isSumEqual(self, firstWord, secondWord, targetWord):
        def word2num(word):
            table = str.maketrans('abcdefghij', '0123456789')
            return int(word.translate(table))
        return word2num(firstWord) + word2num(secondWord) == word2num(targetWord)