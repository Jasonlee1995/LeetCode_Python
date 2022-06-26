class Solution:
    def repeatedNTimes(self, nums):
        step = 3
        for i in range(0, len(nums)-step, step):
            if (nums[i] == nums[i+1]) or (nums[i] == nums[i+2]):
                return nums[i]
            elif nums[i+1] == nums[i+2]:
                return nums[i+1]
        return nums[-1]