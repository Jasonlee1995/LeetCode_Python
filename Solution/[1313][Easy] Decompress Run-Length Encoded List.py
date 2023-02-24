class Solution:
    def decompressRLElist(self, nums):
        answer = []
        for i in range(0, len(nums), 2):
            answer += [nums[i+1]] * nums[i]
        return answer