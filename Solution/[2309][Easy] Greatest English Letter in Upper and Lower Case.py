class Solution:
    def greatestLetter(self, s):
        A, Z, a, z = ord('A'), ord('Z'), ord('a'), ord('z')
        upper = {chr(n) : False for n in range(A, Z+1)}
        lower = {chr(n) : False for n in range(a, z+1)}
        for letter in s:
            if letter in upper: upper[letter] = True
            if letter in lower: lower[letter] = True
        for u_n, l_n in zip(range(Z, A-1, -1), range(z, a-1, -1)):
            u, l = chr(u_n), chr(l_n)
            if upper[u] and lower[l]: return u
        return ""