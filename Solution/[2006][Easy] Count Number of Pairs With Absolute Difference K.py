class Solution:
    def countKDifference(self, nums, k):
        freq = {}
        answer = 0
        for num in nums:
            if num-k in freq: answer += freq[num-k]
            if num+k in freq: answer += freq[num+k]
            freq[num] = freq.get(num, 0) + 1
        return answer