import bisect

class Solution:
    def findKthPositive(self, arr, k):
        return k + bisect.bisect_right(range(len(arr)), k, key=lambda x: arr[x]-x)