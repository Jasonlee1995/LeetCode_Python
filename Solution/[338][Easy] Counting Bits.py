class Solution(object):
    def countBits(self, n):
        answer = [0]
        for num in range(1, n+1):
            answer.append(answer[num//2] + num%2)
        return answer
