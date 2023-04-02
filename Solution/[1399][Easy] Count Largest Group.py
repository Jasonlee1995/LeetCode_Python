import collections


class Solution:
    def countLargestGroup(self, n):
        digit_sum = [0] * (n+1)
        for i in range(1, n+1):
            s, r = i // 10, i % 10
            digit_sum[i] = digit_sum[s] + r
        
        counter = collections.Counter(digit_sum[1:])
        counter_values = list(counter.values())
        counter_max_value = max(counter_values)
        return counter_values.count(counter_max_value)