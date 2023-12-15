class Solution:
    def secondHighest(self, s):
        nums = sorted(set([int(n) for n in s if n.isdigit()]))
        if len(nums) < 2: return -1
        else: return nums[-2]