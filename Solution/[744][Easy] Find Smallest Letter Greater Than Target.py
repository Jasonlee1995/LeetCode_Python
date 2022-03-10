class Solution:
    def nextGreatestLetter(self, letters, target):
        if ord(letters[-1]) <= ord(target): return letters[0]
        idx = [0, len(letters)]
        while idx[0] < idx[1]:
            mid = sum(idx) // 2
            if ord(letters[mid]) <= ord(target): idx[0] = mid+1
            else: idx[1] = mid
        return letters[idx[0]]
