class Solution:
    def findKDistantIndices(self, nums, key, k):
        answer = [-1]
        for j, num in enumerate(nums):
            if num == key:
                for i in range(max(j-k, answer[-1]+1, 0), min(j+k+1, len(nums))):
                    answer.append(i)
        return answer[1:]