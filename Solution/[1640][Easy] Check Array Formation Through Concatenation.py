class Solution:
    def canFormArray(self, arr, pieces):
        dic = {piece[0]:piece for piece in pieces}
        match = []
        for n in arr:
            match += dic.get(n, [])
        return arr == match