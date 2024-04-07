class Solution:
    def minimumDifference(self, nums, k):
        nums.sort()
        diffs = []
        for idx in range(len(nums)-k+1):
            diffs.append(nums[idx+k-1]-nums[idx])
        if len(diffs) == 0: return 0
        return min(diffs)