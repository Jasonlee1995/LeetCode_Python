class Solution:
    def convertToBase7(self, num):
        check_bool = 1 if num > 0 else -1
        num *= check_bool

        stack = []
        while num:
            stack.append(str(num % 7))
            num //= 7

        if len(stack) == 0: stack.append('0')
        return str(check_bool * int(''.join(stack[::-1])))
