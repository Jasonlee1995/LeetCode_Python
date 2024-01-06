class Solution:
    def maxWidthOfVerticalArea(self, points):
        xs = sorted(set(x for (x, _) in points))
        if len(xs) == 1: return 0
        return max(xs[i+1] - xs[i] for i in range(len(xs)-1))