class Solution:
    def addToArrayForm(self, num, k):
        k = [int(n) for n in str(k)]
        if len(num) < len(k): num, k = k, num
        r = 0
        for idx in range(-1, -len(num)-1, -1):
            if abs(idx) <= len(k): num[idx] += k[idx]
            num[idx] += r
            num[idx], r = num[idx]%10, num[idx]//10
            
        return num if r == 0 else [r] + num