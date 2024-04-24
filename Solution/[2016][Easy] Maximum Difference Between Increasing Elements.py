class Solution:
    def maximumDifference(self, nums):
        answer = -1
        curr_min = nums[0]
        for num in nums:
            if curr_min < num: answer = max(answer, num-curr_min)
            else: curr_min = min(curr_min, num)
        return answer