class NumArray:
    def __init__(self, nums):
        self.sums = [nums[0]]
        for idx in range(1, len(nums)):
            self.sums.append(self.sums[-1] + nums[idx])

    def sumRange(self, left, right):
        if left == 0: return self.sums[right]
        return self.sums[right] - self.sums[left-1]
