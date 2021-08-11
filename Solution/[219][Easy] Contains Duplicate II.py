class Solution:
    def containsNearbyDuplicate(self, nums, k):
        num2idx = {}
        for idx, num in enumerate(nums):
            if (num2idx.get(num) != None) and (idx-num2idx[num] <= k): return True
            num2idx[num] = idx
        return False
