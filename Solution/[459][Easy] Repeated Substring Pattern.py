class Solution:
    def repeatedSubstringPattern(self, s):
        return s in s[1:] + s[:-1]
