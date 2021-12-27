class Solution:
    def findMaxAverage(self, nums, k):
        answer = curr = sum(nums[:k])
        for i in range(len(nums)-k):
            curr = curr - nums[i] + nums[i+k]
            answer = max(answer, curr)
        return answer / k
