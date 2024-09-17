class Solution:
    def findClosestNumber(self, nums):
        answer, diff = nums[0], abs(nums[0])
        for num in nums:
            if   abs(num) == diff: answer = max(answer, num)
            elif abs(num) <  diff: answer, diff = num, abs(num)
        return answer