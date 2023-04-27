class Solution:
    def maxPower(self, s):
        cnt = answer = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                cnt += 1
            else:
                answer = max(answer, cnt)
                cnt = 1
        answer = max(answer, cnt)
        return answer