class Solution:
    def searchInsert(self, nums, target):
        start, end = 0, len(nums)-1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < target: start = mid + 1
            else: end = mid
        if target <= nums[start]: return start
        else: return end + 1
