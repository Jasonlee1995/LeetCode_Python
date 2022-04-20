class Solution:
    def lemonadeChange(self, bills):
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five: five, ten = five-1, ten+1
                else: return False
            else:
                if ten and five: five, ten = five-1, ten-1
                elif five >= 3: five -= 3
                else: return False
        return True
