import collections

class Solution:
    def countWords(self, words1, words2):
        counter1, counter2 = collections.Counter(words1), collections.Counter(words2)
        answer = 0
        for word in counter1:
            if (counter1[word] == 1) and (counter2.get(word) == 1):
                answer += 1
        return answer