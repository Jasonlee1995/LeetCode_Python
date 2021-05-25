class Solution:
    def maxSubArray(self, nums):
        answer = [nums[0]]
        for i in range(1, len(nums)):
            if (answer[-1] < 0) and (answer[-1] < nums[i]): answer.append(nums[i])
            else: answer.append(answer[-1] + nums[i])
        return max(answer)
