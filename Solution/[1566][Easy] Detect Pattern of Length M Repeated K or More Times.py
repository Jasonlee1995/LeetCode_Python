class Solution:
    def containsPattern(self, arr, m, k):
        cnt, idx = 0, 0
        while idx < len(arr):
            if arr[idx:idx+m] == arr[idx+m:idx+2*m]:
                if cnt == 0:
                    cnt = 1
                cnt, idx = cnt+1, idx+m
            else:
                cnt, idx = 0, idx+1

            if cnt == k: return True
        return False