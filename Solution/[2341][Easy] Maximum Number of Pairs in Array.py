import collections

class Solution:
    def numberOfPairs(self, nums):
        cnt = collections.Counter(nums)
        answer = [0, 0]
        for num in cnt:
            answer[0] += cnt[num] // 2
            answer[1] += cnt[num] % 2
        return answer