class Solution:
    def prefixesDivBy5(self, nums):
        answer, n = [], 0
        for num in nums:
            n = (n << 1) + num
            answer.append(n % 5 == 0)
        return answer