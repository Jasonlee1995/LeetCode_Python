class Solution:
    def toGoatLatin(self, sentence):
        answer, word, cnt = '', '', 1
        sentence += ' '
        for letter in sentence:
            if letter == ' ':
                if word:
                    if word[0].lower() not in 'aeiou':
                        word = word[1:] + word[:1]
                    answer += word + 'ma' + 'a' * cnt
                    word, cnt = '', cnt+1
                answer += letter
            else:
                word += letter
        return answer[:-1]
