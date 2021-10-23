class Solution:
    def findWords(self, words):
        dic = {}
        for i, row in enumerate(['qwertyuiop', 'asdfghjkl', 'zxcvbnm']):
            for letter in row:
                dic[letter] = i
        answer = []
        for word in words:
            check = dic[word[0].lower()]
            for letter in word:
                if dic[letter.lower()] != check:
                    break
            else:
                answer.append(word)
        return answer
