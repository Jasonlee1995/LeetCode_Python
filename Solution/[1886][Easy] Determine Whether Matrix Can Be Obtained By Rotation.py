class Solution:
    def findRotation(self, mat, target):
        def rotation(mat):
            return [list(col)[::-1] for col in zip(*mat)]
        
        for _ in range(4):
            if mat == target: return True
            mat = rotation(mat)
        return False