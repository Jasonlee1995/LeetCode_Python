class Solution:
    def makeGood(self, s):
        stack = []
        for i in range(len(s)):
            if stack and (stack[-1] == s[i].swapcase()):
                stack.pop()
            else:
                stack.append(s[i])
        return ''.join(stack)