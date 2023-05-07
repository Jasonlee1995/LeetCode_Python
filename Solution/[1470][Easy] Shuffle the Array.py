class Solution:
    def shuffle(self, nums, n):
        answer = []
        for idx in range(n):
            answer += [nums[idx], nums[n+idx]]
        return answer