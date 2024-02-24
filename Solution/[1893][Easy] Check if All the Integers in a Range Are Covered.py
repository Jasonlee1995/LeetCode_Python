class Solution:
    def isCovered(self, ranges, left, right):
        check = [0] * 52
        for start, end in ranges:
            check[start] += 1
            check[end+1] -= 1
        for i in range(1, len(check)):
            check[i] += check[i-1]
        
        return min(check[left:right+1]) > 0