class Solution:
    def reformatNumber(self, number):
        number = number.replace(' ', '').replace('-', '')
        answer = [number[3*i:3*i+3] for i in range((1+len(number)) // 3)]
        if len(number) % 3 == 1:
            answer.pop()
            answer += [number[-4:-2], number[-2:]]
        return '-'.join(answer)