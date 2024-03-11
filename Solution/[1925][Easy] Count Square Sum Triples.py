class Solution:
    def countTriples(self, n):
        answer = 0
        for i in range(1, n):
            for j in range(i+1, n):
                k = (i ** 2 + j ** 2) ** 0.5
                if (int(k) == k) and (k <= n):
                    answer += 1
        return 2*answer