class Solution:
    def diStringMatch(self, s):
        l, h = 0, len(s)
        answer = []
        for i in range(len(s)):
            if s[i] == 'I':
                answer.append(l)
                l += 1
            else:
                answer.append(h)
                h -= 1
        return answer + [l]