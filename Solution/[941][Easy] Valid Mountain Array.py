class Solution:
    def validMountainArray(self, arr):
        i, j, n = 0, len(arr)-1, len(arr)
        while (i < n-1) and (arr[i] < arr[i+1]): i += 1
        while (0 < j)   and (arr[j-1] > arr[j]): j -= 1
        return 0 < i == j < n-1