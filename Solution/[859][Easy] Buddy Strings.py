class Solution:
    def buddyStrings(self, s, goal):
        if len(s) != len(goal): return False
        idxs = [i for i in range(len(s)) if s[i] != goal[i]]
        if len(idxs) == 0: return len(s) != len(set(s))
        elif len(idxs) == 2: return (s[idxs[0]] == goal[idxs[1]]) and (s[idxs[1]] == goal[idxs[0]])
        else: return False
