import collections


class Solution:
    def sortedSquares(self, nums):
        l, r = 0, len(nums)-1
        answer = collections.deque()
        while l < r:
            if abs(nums[l]) <= abs(nums[r]):
                answer.appendleft(nums[r] ** 2)
                r -= 1
            else:
                answer.appendleft(nums[l] ** 2)
                l += 1
        answer.appendleft(nums[l] ** 2)
        return answer