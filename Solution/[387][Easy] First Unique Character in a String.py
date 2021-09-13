class Solution:
    def firstUniqChar(self, s):
        dic = {}
        for idx, letter in enumerate(s):
            if letter not in dic: dic[letter] = []
            dic[letter].append(idx)
        for letter in dic:
            if len(dic[letter]) == 1:
                return dic[letter][0]
        return -1
