class Solution:
    def canMakeArithmeticProgression(self, arr):
        start, end = min(arr), max(arr)
        diff = end - start
        if diff % (len(arr) - 1) != 0: return False

        diff = diff // (len(arr) - 1)
        if diff == 0: return True

        count = [False] * len(arr)
        for num in arr:
            s = num - start
            if s % diff != 0: return False
            
            s = s // diff
            if (s >= len(arr)) or count[s]: return False
            else: count[s] = True
        return True