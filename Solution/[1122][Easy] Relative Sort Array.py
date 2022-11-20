class Solution:
    def relativeSortArray(self, arr1, arr2):
        count = {num : 0 for num in arr2}
        left = []
        for num in arr1:
            if num in count: count[num] += 1
            else: left.append(num)
        
        answer = []
        for num in arr2:
            answer += [num] * count[num]
        return answer + sorted(left)
