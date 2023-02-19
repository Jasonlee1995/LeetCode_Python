class Solution:
    def freqAlphabets(self, s):
        dic = {str(i) : chr(i + 96) for i in range(1, 27)}

        answer = ''
        idx = 0
        while idx < len(s):
            if (idx+2 < len(s)) and (s[idx+2] == '#'):
                answer += dic[s[idx:idx+2]]
                idx += 3
            else:
                answer += dic[s[idx]]
                idx += 1
        return answer