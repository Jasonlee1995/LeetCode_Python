class Solution:
    def twoSum(self, numbers, target):
        idx0, idx1 = 0, len(numbers)-1
        while idx0 < idx1:
            low, high = numbers[idx0], numbers[idx1]
            if low + high > target: idx1 -= 1
            elif low + high < target: idx0 += 1
            else: return [idx0+1, idx1+1]
