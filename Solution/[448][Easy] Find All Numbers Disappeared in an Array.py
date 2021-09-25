class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums: nums[abs(num)-1] = -abs(nums[abs(num)-1])
        return [num+1 for num in range(len(nums)) if nums[num] > 0]
