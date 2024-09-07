class Solution:
    def largestInteger(self, num):
        is_even, evens, odds = [], [], []
        for n in str(num):
            n = int(n)
            if n % 2 == 0: evens.append(n)
            else: odds.append(n)
            is_even.append(n%2 == 0)
        evens.sort(); odds.sort()
        
        answer = ''
        for b in is_even:
            if b: answer += str(evens.pop())
            else: answer += str(odds.pop())
        return int(answer)