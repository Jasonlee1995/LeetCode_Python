class Solution:
    def titleToNumber(self, columnTitle):
        abc = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        answer = 0
        for c in columnTitle:
            answer = 26 * answer + abc.index(c) + 1
        return answer
