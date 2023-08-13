class Solution:
    def maxDepth(self, s):
        answer = 0
        count  = 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
                answer = max(count, answer)
            elif s[i] == ')':
                count -= 1
        return answer