class Solution:
    def checkIfExist(self, arr):
        dic = {}
        for _ in range(2):
            for idx, val in enumerate(arr):
                if 2 * val not in dic:
                    dic[val] = idx
                elif dic[2 * val] != idx:
                    return True
        return False