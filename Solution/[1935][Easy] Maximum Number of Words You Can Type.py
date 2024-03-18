class Solution:
    def canBeTypedWords(self, text, brokenLetters):
        answer = 0
        for word in text.split():
            for broken_letter in brokenLetters:
                if broken_letter in word:
                    break
            else:
                answer += 1
        return answer