class Solution:
    def removeAnagrams(self, words):
        answer = [words[0]]
        last_sword = sorted(words[0])
        for idx in range(1, len(words)):
            sword = sorted(words[idx])
            if last_sword != sword:
                last_sword = sword
                answer.append(words[idx])
        return answer