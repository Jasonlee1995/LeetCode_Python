class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        # (loss-repeat)
        f = n*(n+1)//2 - sum(nums)
        # loss^2 - repeat^2 = (loss+repeat) * (loss-repeat)
        s = n*(n+1)*(2*n+1)//6 - sum(num**2 for num in nums)
        loss, repeat = (s//f + f)//2, (s//f - f)//2
        return [repeat, loss]
