class Solution:
    def removeDuplicates(self, s):
        stack = []
        for abc in s:
            if stack and stack[-1] == abc: stack.pop()
            else: stack.append(abc)
        return ''.join(stack)