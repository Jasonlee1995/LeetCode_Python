import collections

class Solution:
    def kthDistinct(self, arr, k):
        cnt = collections.Counter(arr)
        stack = [s for s in arr if cnt[s] == 1]
        if len(stack) < k: return ""
        return stack[k-1]