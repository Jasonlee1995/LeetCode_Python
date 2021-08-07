class Solution:
    def countPrimes(self, n):
        if n < 2: return 0
        primes = [False, False] + [True] * (n-2)
        for i in range(2, int(n ** 0.5)+1):
            if primes[i]:
                for j in range(2*i, n, i):
                    primes[j] = False
        return sum(primes)
