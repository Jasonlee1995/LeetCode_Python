import collections


class Solution:
    def numIdenticalPairs(self, nums):
        counter = collections.Counter(nums)
        answer = 0
        for num in counter:
            n = counter[num]
            answer += (n * (n-1)) // 2
        return answer