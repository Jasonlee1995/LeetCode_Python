class Solution:
    def mostCommonWord(self, paragraph, banned):
        dic = {}
        word = ''
        for letter in paragraph.lower():
            if letter not in ''' "!?',;.''':
                word += letter
            elif word:
                dic[word] = dic.get(word, 0) + 1
                word = ''
        if word:
            dic[word] = dic.get(word, 0) + 1

        for k, v in sorted(dic.items(), key=lambda x: -x[1]):
            if k not in banned:
                return k
