class Solution:
    def thirdMax(self, nums):
        nums = set(nums)
        if len(nums) < 3: return max(nums)

        top3 = [None, None, None]
        for num in nums:
            if (top3[0] == None) or (top3[0] < num): top3 = [num] + top3[:2]
            elif (top3[1] == None) or (top3[1] < num): top3 = [top3[0], num, top3[1]]
            elif (top3[2] == None) or (top3[2] < num): top3 = top3[:2] + [num]
        return top3[-1]
