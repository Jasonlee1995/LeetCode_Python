class Solution:
    def summaryRanges(self, nums):
        answer, stack = [], []
        for num in nums:
            if (len(stack) == 0) or (stack[-1][1]+1 != num): stack.append((num, num))
            else: stack[-1] = (stack[-1][0], stack[-1][1]+1)
        for start, end in stack:
            if start == end: answer.append(str(start))
            else: answer.append('{}->{}'.format(start, end))
        return answer
