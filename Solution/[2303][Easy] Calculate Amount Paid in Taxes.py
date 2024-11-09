class Solution:
    def calculateTax(self, brackets, income):
        answer = prev = 0
        for upper, percent in brackets:
            if income > upper:
                answer += (upper - prev) * percent / 100
                prev = upper
            else:
                answer += (income - prev) * percent / 100
                break
        return answer