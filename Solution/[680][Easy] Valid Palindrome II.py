class Solution:
    def validPalindrome(self, s):
        left, right = 0, len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1; right -= 1
            else:
                l, r = s[left+1:right+1], s[left:right]
                return (l == l[::-1]) or (r == r[::-1])
        return True
