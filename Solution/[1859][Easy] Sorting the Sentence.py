class Solution:
    def sortSentence(self, s):
        s = s.split()
        sentences = [None] * len(s)
        for wordnum in s:
            word, num = wordnum[:-1], int(wordnum[-1])
            sentences[num-1] = word
        return ' '.join(sentences)