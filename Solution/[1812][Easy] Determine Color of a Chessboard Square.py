class Solution:
    def squareIsWhite(self, coordinates):
        alpha = 'abcdefgh'
        digit = '12345678'
        a, d = coordinates
        return (alpha.index(a) + digit.index(d)) % 2 == 1