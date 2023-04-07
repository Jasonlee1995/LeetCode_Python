class Solution:
    def stringMatching(self, words):
        words.sort(key=lambda x: len(x))
        answer = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    answer.append(words[i])
                    break
        return answer