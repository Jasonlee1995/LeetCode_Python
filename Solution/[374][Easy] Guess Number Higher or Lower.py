# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        l, r = 1, n
        while r > l:
            mid = (l+r)//2
            if guess(mid) == -1: r = mid-1
            elif guess(mid) == 1: l = mid+1
            else: return mid
        return l
