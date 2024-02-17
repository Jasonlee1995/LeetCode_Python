class Solution:
    def countGoodSubstrings(self, s):
        answer = 0
        for i in range(len(s)):
            if len(set(s[i:i+3])) == 3:
                answer += 1
        return answer