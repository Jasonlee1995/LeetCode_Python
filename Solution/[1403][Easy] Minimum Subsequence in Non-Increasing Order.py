class Solution:
    def minSubsequence(self, nums):
        nums.sort(reverse=True)
        curr, left = 0, sum(nums)
        answer = []
        for num in nums:
            if curr > left: break
            curr, left = curr + num, left - num
            answer.append(num)
        return answer