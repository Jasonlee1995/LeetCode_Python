class Solution:
    def fizzBuzz(self, n):
        answer = []
        for idx in range(1, n+1):
            temp = ''
            if idx%3 == 0: temp += 'Fizz'
            if idx%5 == 0: temp += 'Buzz'
            if len(temp) == 0: temp += str(idx)
            answer.append(temp)
        return answer
