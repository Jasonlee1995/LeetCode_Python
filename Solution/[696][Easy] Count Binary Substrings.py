class Solution:
    def countBinarySubstrings(self, s):
        answer = [1]
        for i in range(1, len(s)):
            if s[i] == s[i-1]: answer[-1] += 1
            else: answer.append(1)

        count = 0
        for i in range(1, len(answer)):
            count += min(answer[i-1], answer[i])
        return count
