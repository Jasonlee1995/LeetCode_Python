class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        answer = []
        m = None
        for i in range(len(arr)-1):
            if m == None:
                answer.append([arr[i], arr[i+1]])
                m = arr[i+1] - arr[i]
            elif arr[i+1] - arr[i] == m:
                answer.append([arr[i], arr[i+1]])
            elif arr[i+1] - arr[i] < m:
                answer = [[arr[i], arr[i+1]]]
                m = arr[i+1] - arr[i]
        return answer