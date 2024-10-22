class Solution:
    def percentageLetter(self, s, letter):
        return (100 * s.count(letter)) // len(s)