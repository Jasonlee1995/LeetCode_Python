class Solution:
    def createTargetArray(self, nums, index):
        answer = []
        for num, idx in zip(nums, index):
            answer.insert(idx, num)
        return answer