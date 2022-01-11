class Solution:
    def imageSmoother(self, img):
        m, n = len(img), len(img[0])
        matrix = [[] for _ in range(m)]

        # padding
        for r in range(m): img[r] = [-1] + img[r] + [-1]
        img = [[-1] * (n+2)] + img + [[-1] * (n+2)]

        for r in range(1, m+1):
            for c in range(1, n+1):
                total = img[r-1][c-1:c+2] + img[r][c-1:c+2] + img[r+1][c-1:c+2]
                cnt = total.count(-1)
                val = (sum(total) + cnt) // (len(total) - cnt)
                matrix[r-1].append(val)
        return matrix
