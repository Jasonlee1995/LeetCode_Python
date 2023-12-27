class Solution:
    def numDifferentIntegers(self, word):
        nums = set()
        num  = ''
        for s in word:
            if s.isdigit():
                num += s
            elif num:
                nums.add(int(num))
                num = ''
        if num: nums.add(int(num))
        return len(nums)