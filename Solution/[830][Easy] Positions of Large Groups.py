class Solution:
    def largeGroupPositions(self, s):
        answer, idx, cnt = [], None, 1
        s += ' '
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cnt += 1
            else:
                if cnt >= 3: answer.append([idx, i-1])
                cnt = 1

            if cnt == 3: idx = i-2
        return answer
