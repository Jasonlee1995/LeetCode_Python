class Solution:
    def makeFancyString(self, s):
        stack = []
        for abc in s:
            if (len(stack) < 2) or (abc != stack[-1]) or (abc != stack[-2]):
                stack.append(abc)
        return ''.join(stack)