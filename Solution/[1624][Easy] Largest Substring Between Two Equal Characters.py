class Solution:
    def maxLengthBetweenEqualCharacters(self, s):
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic: dic[s[i]] = []
            dic[s[i]].append(i)
        
        answer = -1
        for letter in dic:
            if len(dic[letter]) > 1:
                start, end = dic[letter][0], dic[letter][-1]
                count = end - start - 1
                answer = max(answer, count)
        return answer