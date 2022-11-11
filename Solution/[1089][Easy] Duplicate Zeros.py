class Solution:
    def duplicateZeros(self, arr):
        stack = []
        for n in arr:
            stack.append(n)
            if n == 0: stack.append(n)
        arr[:] = stack[:len(arr)]