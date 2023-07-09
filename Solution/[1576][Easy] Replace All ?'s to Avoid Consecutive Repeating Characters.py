class Solution:
    def modifyString(self, s):
        stack = list(s)
        for i in range(len(s)):
            if stack[i] == '?':
                for abc in 'abc':
                    if abc not in stack[max(i-1, 0):i+2]:
                        stack[i] = abc
                        break
        return ''.join(stack)