class Solution:
    def kLengthApart(self, nums, k):
        last_idx = -1
        for idx in range(len(nums)):
            if nums[idx] == 1:
                if (last_idx != -1) and (idx - last_idx - 1 < k):
                    return False
                last_idx = idx
        return True