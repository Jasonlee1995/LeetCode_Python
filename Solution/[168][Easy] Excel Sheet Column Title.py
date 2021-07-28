class Solution:
    def convertToTitle(self, columnNumber):
        letters = [chr(letter) for letter in range(ord('A'), ord('Z')+1)]
        answer = ''
        while columnNumber:
            columnNumber -= 1
            columnNumber, r = columnNumber//26, columnNumber%26
            answer += letters[r]
        return answer[::-1]
