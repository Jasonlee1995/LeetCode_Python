class Solution:
    def numOfStrings(self, patterns, word):
        return sum(1 for pattern in patterns if pattern in word)