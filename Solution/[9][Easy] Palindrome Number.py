class Solution:
    def isPalindrome(self, x):
        if (x < 0) or ((x > 0) and (x%10 == 0)): return False
        rev_x = 0
        while x > rev_x:
            rev_x = 10*rev_x + x%10
            x = x//10
        if (x == rev_x) or (x == rev_x//10): return True
        return False
