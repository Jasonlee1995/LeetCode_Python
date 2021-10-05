class Solution:
    def findMaxConsecutiveOnes(self, nums):
        answer, count = 0, 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                answer = max(answer, count)
                count = 0
        return max(answer, count)
