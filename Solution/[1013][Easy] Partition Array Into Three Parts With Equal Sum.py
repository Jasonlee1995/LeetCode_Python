class Solution:
    def canThreePartsEqualSum(self, arr):
        total = sum(arr)
        if total % 3 != 0: return False

        cnt, cumsum, average = 0, 0, total // 3
        for i in range(len(arr)):
            cumsum += arr[i]
            if cumsum == average:
                cnt += 1
                cumsum = 0
        return cnt >= 3