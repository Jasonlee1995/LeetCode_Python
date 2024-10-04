class Solution:
    def removeDigit(self, number, digit):
        last_idx = None
        for idx in range(len(number)):
            if number[idx] == digit:
                last_idx = idx
                if (idx+1 < len(number)) and (number[idx] < number[idx+1]):
                    break
        return number[:last_idx] + number[last_idx+1:]