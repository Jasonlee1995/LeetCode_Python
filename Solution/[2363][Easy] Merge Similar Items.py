class Solution:
    def mergeSimilarItems(self, items1, items2):
        dic = {}
        for v, w in items1 + items2:
            if v not in dic: dic[v] = 0
            dic[v] += w
        return sorted(dic.items())