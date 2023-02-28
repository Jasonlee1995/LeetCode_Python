class Solution:
    def maximum69Number (self, num):
        num_copy = num
        idx_curr, idx_6 = 0, None
        while num_copy:
            num_copy, remainder = num_copy // 10, num_copy % 10
            if remainder == 6:
                idx_6 = idx_curr
            idx_curr += 1
        
        if idx_6 is not None: return num + 3 * (10 ** idx_6)
        else: return num