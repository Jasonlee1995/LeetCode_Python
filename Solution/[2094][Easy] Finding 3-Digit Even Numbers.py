import collections

class Solution:
    def findEvenNumbers(self, digits):
        cnt = collections.Counter(digits)
        answer = []
        for num in range(100, 999, 2):
            curr_cnt = collections.Counter([int(n) for n in str(num)])
            diff_cnt = curr_cnt - cnt
            if len(diff_cnt) == 0:
                answer.append(num)
        return answer