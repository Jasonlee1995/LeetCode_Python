import collections


class Solution:
    def longestPalindrome(self, s):
        letters = collections.Counter(s)
        answer, odd = 0, False
        for letter in letters:
            answer += letters[letter]
            if letters[letter] % 2 == 1:
                if odd: answer -= 1
                else: odd = True
        return answer
