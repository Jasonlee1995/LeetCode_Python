class Solution:
    def findNumbers(self, nums):
        def count_digit(num):
            digit = 0
            while num:
                num = num // 10
                digit += 1
            return digit
        
        return sum(count_digit(num) % 2 == 0 for num in nums)