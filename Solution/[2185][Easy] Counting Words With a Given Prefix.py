class Solution:
    def prefixCount(self, words, pref):
        return sum(word.startswith(pref) for word in words)