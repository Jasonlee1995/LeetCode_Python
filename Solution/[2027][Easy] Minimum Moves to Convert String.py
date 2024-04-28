class Solution:
    def minimumMoves(self, s):
        answer = 0
        idx = 0
        while idx < len(s):
            if s[idx] == 'X':
                answer += 1
                idx += 3
            else:
                idx += 1
        return answer