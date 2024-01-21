class Solution:
    def arraySign(self, nums):
        answer = 1
        for num in nums:
            if   num == 0: return 0
            elif num <  0: answer *= -1
        return answer