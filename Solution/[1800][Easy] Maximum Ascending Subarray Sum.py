class Solution:
    def maxAscendingSum(self, nums):
        stack  = []
        answer = 0
        for num in nums:
            if stack and (stack[-1] >= num):
                answer = max(answer, sum(stack))
                stack  = []
            stack.append(num)
        if stack:
            answer = max(answer, sum(stack))
        return answer