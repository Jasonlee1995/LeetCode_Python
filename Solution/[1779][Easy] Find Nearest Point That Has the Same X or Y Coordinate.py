import math

class Solution:
    def nearestValidPoint(self, x, y, points):
        answer, value = -1, math.inf
        for idx, (a, b) in enumerate(points):
            dx, dy = x-a, y-b
            if (dx * dy == 0) and (abs(dx+dy) < value):
                answer, value = idx, abs(dx+dy)
        return answer