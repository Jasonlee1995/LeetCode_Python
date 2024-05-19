class Solution:
    def areNumbersAscending(self, s):
        nums = [int(token) for token in s.split() if token.isdigit()]
        return all(nums[idx] < nums[idx+1] for idx in range(len(nums)-1))