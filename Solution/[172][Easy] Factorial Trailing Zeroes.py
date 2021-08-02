class Solution:
    def trailingZeroes(self, n):
        answer, state = 0, 5
        while state <= n:
            answer += n//state
            state *= 5
        return answer
