class Solution:
    def addBinary(self, a, b):
        a, b = list(a), list(b)
        answer = ''
        cache = 0
        while a or b or cache:
            if a: cache += int(a.pop())
            if b: cache += int(b.pop())
            answer += str(cache % 2)
            cache = cache // 2
        return answer[::-1]
