class Solution:
    def toHex(self, num):
        if num == 0: return '0'

        abc = '0123456789abcdef'
        answer = ''
        if num < 0: num += 2 ** 32
        while num:
            answer += abc[num % 16]
            num = num//16
        return answer[::-1]
