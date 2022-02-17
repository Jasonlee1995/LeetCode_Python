from collections import Counter


class Solution:
    def findLHS(self, nums):
        answer = 0
        nums_info = Counter(nums)
        for num in nums_info:
            if num+1 in nums_info:
                answer = max(answer, nums_info[num] + nums_info[num+1])
        return answer
