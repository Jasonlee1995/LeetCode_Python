class Solution:
    def isPalindrome(self, s):
        l, r = 0, len(s)-1
        s = s.lower()
        while l < r:
            while (l < r) and (not s[l].isalnum()): l += 1
            while (l < r) and (not s[r].isalnum()): r -= 1
            if s[l] != s[r]: return False
            else: l, r = l+1, r-1
        return True
