class Solution:
    def numJewelsInStones(self, jewels, stones):
        return sum(stones.count(j) for j in jewels)
