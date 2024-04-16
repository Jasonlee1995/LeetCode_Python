class Solution:
    def reversePrefix(self, word, ch):
        if ch in word:
            idx = word.index(ch)
            word = word[:idx+1][::-1] + word[idx+1:]
        return word