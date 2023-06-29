class Solution:
    def thousandSeparator(self, n):
        num = list(str(n)[::-1])
        stack = []
        for i in range(len(num)):
            if (i > 0) and (i % 3 == 0):
                stack.append('.')
            stack.append(num[i])
        return ''.join(stack)[::-1]