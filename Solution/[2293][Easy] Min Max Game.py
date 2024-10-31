class Solution:
    def minMaxGame(self, nums):
        while len(nums) > 1:
            stack = []
            for idx in range(len(nums) // 2):
                if idx % 2 == 0: stack.append(min(nums[2*idx], nums[2*idx+1]))
                else:            stack.append(max(nums[2*idx], nums[2*idx+1]))
            nums = stack
        return nums[0]