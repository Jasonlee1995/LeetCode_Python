class Solution:
    def countOperations(self, num1, num2):
        num1, num2 = max(num1, num2), min(num1, num2)
        answer = 0
        while num1 and num2:
            s, r = num1 // num2, num1 % num2
            answer += s
            num1, num2 = num2, r
        return answer