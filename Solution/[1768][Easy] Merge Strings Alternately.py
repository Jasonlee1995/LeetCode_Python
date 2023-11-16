import itertools

class Solution:
    def mergeAlternately(self, word1, word2):
        return ''.join(w1+w2 for w1,w2 in itertools.zip_longest(word1, word2, fillvalue=''))