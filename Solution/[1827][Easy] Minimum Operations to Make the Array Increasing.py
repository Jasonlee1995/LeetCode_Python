class Solution:
    def minOperations(self, nums):
        answer = 0
        for idx in range(1, len(nums)):
            if nums[idx-1] >= nums[idx]:
                dt = nums[idx-1] - nums[idx] + 1
                answer += dt
                nums[idx] += dt
        return answer