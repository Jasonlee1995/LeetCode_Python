class Solution:
    def balancedStringSplit(self, s):
        answer = count = 0
        for LR in s:
            if LR == 'L': count -= 1
            if LR == 'R': count += 1
            if count == 0: answer += 1
        return answer