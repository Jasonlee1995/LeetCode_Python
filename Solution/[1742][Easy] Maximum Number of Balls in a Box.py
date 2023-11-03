class Solution:
    def countBalls(self, lowLimit, highLimit):
        dic = {}
        for n in range(lowLimit, highLimit+1):
            n = sum(map(int, str(n)))
            dic[n] = dic.get(n, 0) + 1
        return max(dic.values())