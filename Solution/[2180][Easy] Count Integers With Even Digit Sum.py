class Solution:
    def countEven(self, num):
        return (num - sum(map(int, str(num))) % 2) // 2