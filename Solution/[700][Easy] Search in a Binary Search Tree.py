class Solution:
    def findShortestSubArray(self, nums):
        dic = {}
        for idx, num in enumerate(nums):
            if num not in dic: dic[num] = []
            dic[num].append(idx)

        degree, answer = 0, 0
        for num in dic:
            n = len(dic[num])
            if n > degree:
                degree = n
                answer = dic[num][-1] - dic[num][0] + 1
            elif n == degree:
                answer = min(answer, dic[num][-1] - dic[num][0] + 1)
        return answer
