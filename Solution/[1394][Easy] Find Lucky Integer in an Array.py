import collections


class Solution:
    def findLucky(self, arr):
        counter = collections.Counter(arr)
        answer = -1
        for key in counter:
            if key == counter[key]:
                answer = max(answer, key)
        return answer