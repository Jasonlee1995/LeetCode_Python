class Solution:
    def cellsInRange(self, s):
        c0, r0, _, c1, r1 = s
        r0, r1 = int(r0), int(r1)
        answer = []
        for col in range(ord(c0), ord(c1)+1):
            for row in range(r0, r1+1):
                answer.append(chr(col) + str(row))
        return answer