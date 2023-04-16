class Solution:
    def maxScore(self, s):
        left = int(s[0] == '0')
        right = s[1:].count('1')
        answer = left + right
        for i in range(1, len(s)-1):
            if s[i] == '0': left += 1
            else: right -= 1
            answer = max(answer, left+right)
        return answer