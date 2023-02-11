class Solution:
    def replaceElements(self, arr):
        num = -1
        for i in range(len(arr)-1, -1, -1):
            arr[i], num = num, max(arr[i], num)
        return arr