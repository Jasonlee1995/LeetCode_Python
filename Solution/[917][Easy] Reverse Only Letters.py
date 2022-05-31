class Solution:
    def reverseOnlyLetters(self, s):
        i, j = 0, len(s)-1
        s = list(s)
        while i < j:
            ci, cj = s[i].isalpha(), s[j].isalpha()
            if ci and cj:
                s[i], s[j] = s[j], s[i]
                i, j = i+1, j-1
            else:
                if not ci: i += 1
                if not cj: j -= 1
        return ''.join(s)