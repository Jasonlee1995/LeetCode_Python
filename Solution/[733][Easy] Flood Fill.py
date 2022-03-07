class Solution:
    def floodFill(self, image, sr, sc, newColor):
        R, C, origin = len(image), len(image[0]), image[sr][sc]
        if origin == newColor: return image
        stack = [(sr, sc)]
        while stack:
            r, c = stack.pop()
            if (0 <= r < R) and (0 <= c < C) and (image[r][c] == origin):
                image[r][c] = newColor
                stack += [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        return image
