#Shoelace formula
import itertools


class Solution:
    def largestTriangleArea(self, points):
        answer = 0
        for p1, p2, p3 in itertools.combinations(points, 3):
            area = lambda a, b, c: abs(a[0]*b[1] - a[1]*b[0] + b[0]*c[1]- b[1]*c[0] + c[0]*a[1] - c[1]*a[0]) / 2
            answer = max(answer, area(p1, p2, p3))
        return answer
