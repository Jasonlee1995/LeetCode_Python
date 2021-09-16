class Solution:
    def readBinaryWatch(self, turnedOn):
        if turnedOn > 8: return []
        stack = [(turnedOn, [])]
        answer = []
        while stack:
            count, h_m = stack.pop()
            if (len(h_m) > 10) or (count < 0): continue
            elif count == 0:
                h, m = 0, 0
                for idx, t in enumerate(h_m):
                    if idx < 4: h += t * 2 ** (3-idx)
                    else: m += t * 2 ** (9-idx)
                if (h > 11) or (m > 59): continue
                else: answer.append('{}:{}'.format(str(h), str(m).zfill(2)))
            else: stack += [(count, h_m + [0]), (count-1, h_m + [1])]
        return answer
