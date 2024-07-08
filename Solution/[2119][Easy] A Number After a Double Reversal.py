class Solution:
    def isSameAfterReversals(self, num):
        return (num == 0) or (num % 10 != 0)