class Solution:
    def makeEqual(self, words):
        dic = {}
        for word in words:
            for abc in word:
                dic[abc] = dic.get(abc, 0) + 1
        
        l = len(words)
        for abc in dic:
            if dic[abc] % l != 0:
                return False
        return True