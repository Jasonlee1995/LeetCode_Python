class Solution:
    def findOcurrences(self, text, first, second):
        t = text.split()
        answer = []
        for i in range(len(t)-2):
            if (t[i] == first) and (t[i+1] == second):
                answer.append(t[i+2])
        return answer