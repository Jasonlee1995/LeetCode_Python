class Solution:
    def longestNiceSubstring(self, s):
        if len(s) <= 1: return ''
        
        all_cases = set(s)
        weird_letter = set(letter for letter in all_cases if letter.swapcase() not in all_cases)

        if len(weird_letter) == 0:
            return s

        for i in range(len(s)):
            if s[i] in weird_letter:
                break
        
        s0, s1 = self.longestNiceSubstring(s[:i]), self.longestNiceSubstring(s[i+1:])
        if len(s1) > len(s0): return s1
        else: return s0