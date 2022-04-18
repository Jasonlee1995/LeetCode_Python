class Solution:
    def peakIndexInMountainArray(self, arr):
        idx1, idx2 = 0, len(arr)-1
        while idx1 < idx2:
            mid = (idx1+idx2)//2
            if arr[mid] < arr[mid+1]: idx1 = mid+1
            else: idx2 = mid
        return idx1
