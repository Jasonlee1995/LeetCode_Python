class Solution:
    def arithmeticTriplets(self, nums, diff):
        nums_set = set()
        answer   = 0
        for num in nums:
            if (num-diff in nums_set) and (num-2*diff in nums_set):
                answer += 1
            nums_set.add(num)
        return answer