import re

class Solution:
    def strongPasswordCheckerII(self, password):
        cond1 = len(password) >= 8
        cond2 = re.search(r'[a-z]', password) != None
        cond3 = re.search(r'[A-Z]', password) != None
        cond4 = re.search(r'[0-9]', password) != None
        cond5 = re.search(r'[\!\@\#\$\%\^\&\*\(\)\-\+]', password) != None
        cond6 = bool(sum(1 for idx in range(len(password)-1) if password[idx] == password[idx+1]))
        return cond1 and cond2 and cond3 and cond4 and cond5 and (not cond6)