class Solution:
    def findSpecialInteger(self, arr):
        n = len(arr) // 4
        for i in range(len(arr)):
            if arr[i] == arr[i + n]:
                return arr[i]