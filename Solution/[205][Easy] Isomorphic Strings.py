class Solution:
    def isIsomorphic(self, s, t):
        s_info, t_info = {}, {}
        s_idx, t_idx = 0, 0
        for s_, t_ in zip(s, t):
            if s_info.get(s_) == None:
                s_info[s_] = s_idx
                s_idx += 1
            if t_info.get(t_) == None:
                t_info[t_] = t_idx
                t_idx += 1
            if s_info[s_] != t_info[t_]: return False
        return True
