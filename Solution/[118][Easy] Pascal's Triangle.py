class Solution:
    def generate(self, numRows):
        answer = [[1] * (n+1) for n in range(numRows)]
        for i in range(2, len(answer)):
            for j in range(1, len(answer[i])-1):
                answer[i][j] = answer[i-1][j-1] + answer[i-1][j]
        return answer
