class Solution:
    def mostWordsFound(self, sentences):
        return max([len(sentence.split()) for sentence in sentences])