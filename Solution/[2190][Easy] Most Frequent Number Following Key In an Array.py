class Solution:
    def mostFrequent(self, nums, key):
        dic = {}
        for idx, num in enumerate(nums):
            if (num == key) and (idx+1 < len(nums)):
                dic[nums[idx+1]] = dic.get(nums[idx+1], 0) + 1
        return sorted(dic.items(), key=lambda x: -x[1])[0][0]