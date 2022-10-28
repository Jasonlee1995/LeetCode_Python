class Solution:
    def isBoomerang(self, points):
        a, b, c = points
        xa, ya, xb, yb, xc, yc = *a, *b, *c
        return (yb - ya) * (xc - xb) != (xb - xa) * (yc - yb)