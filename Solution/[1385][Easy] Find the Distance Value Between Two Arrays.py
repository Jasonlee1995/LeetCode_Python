class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        arr1.sort()
        arr2.sort()
        idx1, idx2 = 0, 0
        cnt = 0
        while (idx1 < len(arr1)) and (idx2 < len(arr2)):
            if abs(arr1[idx1] - arr2[idx2]) <= d:
                idx1 += 1
            elif arr1[idx1] < arr2[idx2]:
                cnt += 1
                idx1 += 1
            else:
                idx2 += 1
        return cnt + len(arr1) - idx1