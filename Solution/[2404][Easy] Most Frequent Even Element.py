import collections

class Solution:
    def mostFrequentEven(self, nums):
        cnt = collections.Counter(nums)
        answer, freq = -1, 0
        for num in sorted(cnt):
            if (num % 2 == 0) and (cnt[num] > freq):
                answer, freq = num, cnt[num]
        return answer