class Solution:
    def fillCups(self, amount):
        return max(max(amount), (1 + sum(amount)) // 2)