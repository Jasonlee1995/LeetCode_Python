class Solution:
    def minTimeToVisitAllPoints(self, points):
        answer = 0
        for i in range(len(points)-1):
            x0, y0 = points[i]
            x1, y1 = points[i+1]
            dx, dy = abs(x1-x0), abs(y1-y0)
            answer += max(dx, dy)
        return answer