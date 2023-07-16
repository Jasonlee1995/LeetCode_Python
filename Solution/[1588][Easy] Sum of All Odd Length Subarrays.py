class Solution:
    def sumOddLengthSubarrays(self, arr):
        answer = 0
        n = len(arr)
        for i in range(n):
            answer += arr[i] * (((i+1) * (n-i) + 1) // 2)
        return answer