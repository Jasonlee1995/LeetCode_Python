class Solution:
    def romanToInt(self, s):
        info = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        answer = 0
        for i in range(len(s)):
            if (i > 0) and (info[s[i]] > info[s[i-1]]):
                answer -= 2*info[s[i-1]]
            answer += info[s[i]]
        return answer
