class Solution:
    def countHillValley(self, nums):
        slopes = [num1 - num0 for num0, num1 in zip(nums, nums[1:]) if num0 != num1]
        answer = sum(slope0 * slope1 < 0 for slope0, slope1 in zip(slopes, slopes[1:]))
        return answer