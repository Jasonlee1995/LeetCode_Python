class Solution:
    def countQuadruplets(self, nums):
        diff2idx = {}
        answer = 0
        for c in range(len(nums)-2, 1, -1):
            for d in range(c+1, len(nums)):
                diff = nums[d] - nums[c]
                diff2idx[diff] = diff2idx.get(diff, 0) + 1

            b = c-1
            for a in range(b-1, -1, -1):
                ab = nums[a] + nums[b]
                answer += diff2idx.get(ab, 0)
        return answer