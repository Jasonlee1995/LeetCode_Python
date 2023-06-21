class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        answer = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if abs(arr[i]-arr[j]) <= a:
                    for k in range(j+1, len(arr)):
                        if (abs(arr[j]-arr[k]) <= b) and (abs(arr[i]-arr[k]) <= c):
                            answer += 1
        return answer