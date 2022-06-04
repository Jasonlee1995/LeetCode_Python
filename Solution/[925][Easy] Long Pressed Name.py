class Solution:
    def isLongPressedName(self, name, typed):
        i, n = 0, len(name)
        for j in range(len(typed)):
            if (i < n) and (name[i] == typed[j]):
                i += 1
            elif (j == 0) or (typed[j] != typed[j-1]):
                return False
        return i == n