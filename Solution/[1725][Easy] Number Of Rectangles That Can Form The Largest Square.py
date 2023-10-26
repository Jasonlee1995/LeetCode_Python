class Solution:
    def countGoodRectangles(self, rectangles):
        squares = [min(l, w) for l, w in rectangles]
        return squares.count(max(squares))