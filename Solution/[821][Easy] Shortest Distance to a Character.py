class Solution:
    def shortestToChar(self, s, c):
        answer = []
        p = -len(s)

        for i, letter in enumerate(s):
            if letter == c: p = i
            answer.append(i - p)

        for i in range(p, -1, -1):
            if answer[i] == 0: p = i
            answer[i] = min(answer[i], p-i)

        return answer
