class Solution:
    def findLengthOfLCIS(self, nums):
        answer, save_idx = 1, 0
        for idx in range(1, len(nums)):
            if nums[idx] <= nums[idx-1]:
                save_idx = idx
            answer = max(answer, idx-save_idx+1)
        return answer
