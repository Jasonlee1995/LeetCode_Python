class Solution:
    def removeOuterParentheses(self, s):
        answer, first = '', 0
        for string in s:
            if (string == '(') and (first > 0):
                answer += string
            elif (string == ')') and (first > 1):
                answer += string
            first += (string == '(') - (string == ')')
        return answer