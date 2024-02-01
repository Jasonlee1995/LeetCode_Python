class Solution:
    def replaceDigits(self, s):
        stack = []
        for idx in range(len(s)):
            if idx % 2 == 0:
                stack.append(s[idx])
            else:
                stack.append(chr(ord(stack[-1]) + int(s[idx])))
        return ''.join(stack)