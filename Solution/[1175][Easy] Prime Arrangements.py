class Solution:
    def numPrimeArrangements(self, n):
        m = 10 ** 9 + 7
        check = [False, False] + [True] * (n-1)
        for i in range(2, int(n ** 0.5) + 1):
            for j in range(2*i, n+1, i):
                check[j] = False
        
        primes = sum(check)
        non_primes = n - primes
        answer = 1
        for i in range(non_primes, 1, -1):
            answer *= i
            answer %= m
        for i in range(primes, 1, -1):
            answer *= i
            answer %= m
        return answer