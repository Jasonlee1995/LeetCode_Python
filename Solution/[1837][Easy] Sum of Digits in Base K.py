class Solution:
    def sumBase(self, n, k):
        answer = 0
        while n:
            answer += n%k
            n = n//k
        return answer