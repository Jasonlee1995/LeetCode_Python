class Solution:
    def countPairs(self, nums, k):
        num2idx = {}
        for idx, num in enumerate(nums):
            if num not in num2idx: num2idx[num] = []
            num2idx[num].append(idx)

        answer = 0
        for idxs in num2idx.values():
            for i in range(len(idxs)):
                for j in range(i+1, len(idxs)):
                    if (idxs[i] * idxs[j]) % k == 0:
                        answer += 1
        return answer