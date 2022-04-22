class Solution:
    def binaryGap(self, n):
        answer, idx = 0, None
        for i, num in enumerate(bin(n)[2:]):
            if num == '1':
                if idx != None: answer = max(answer, i-idx)
                idx = i
        return answer
