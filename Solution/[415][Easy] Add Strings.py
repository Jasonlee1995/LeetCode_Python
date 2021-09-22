class Solution:
    def addStrings(self, num1, num2):
        num1, num2 = num1.zfill(max(len(num1), len(num2))), num2.zfill(max(len(num1), len(num2)))
        answer, carry, default = '', 0, 2*ord('0')
        for n1, n2 in zip(num1[::-1], num2[::-1]):
            int1, int2 = ord(n1), ord(n2)
            total = int1 + int2 + carry - default
            answer = str(total % 10) + answer
            carry = total // 10
        if carry: answer = str(carry) + answer
        return answer
