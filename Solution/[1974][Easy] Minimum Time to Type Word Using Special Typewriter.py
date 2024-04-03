class Solution:
    def minTimeToType(self, word):
        answer = len(word)
        abcs = 26
        prev = 'a'
        for letter in word:
            path1 = (ord(letter) - ord(prev)) % abcs
            path2 = abcs - path1
            answer += min(path1, path2)
            prev = letter
        return answer