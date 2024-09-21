class Solution:
    def digitSum(self, s, k):
        while len(s) > k:
            next_s = ""
            for idx in range(0, len(s), k):
                next_s += str(sum([int(num) for num in s[idx:idx+k]]))
            s = next_s
        return s