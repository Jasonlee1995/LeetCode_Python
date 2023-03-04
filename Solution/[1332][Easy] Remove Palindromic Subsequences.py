class Solution:
    def removePalindromeSub(self, s):
        return 2 - int(s == s[::-1])