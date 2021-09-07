class Solution(object):
    def reverseVowels(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        idx0, idx1 = 0, len(s)-1
        s = list(s)
        while idx0 <= idx1:
            vowel0, vowel1 = (s[idx0] in vowels), (s[idx1] in vowels)
            if vowel0 and vowel1:
                s[idx0], s[idx1] = s[idx1], s[idx0]
                idx0, idx1 = idx0+1, idx1-1
            elif vowel0: idx1 -= 1
            elif vowel1: idx0 += 1
            else: idx0, idx1 = idx0+1, idx1-1
        return ''.join(s)
