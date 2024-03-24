class Solution:
    def isThree(self, n):
        def is_prime(num):
            for n in range(2, int(num ** 0.5)+1):
                if num % n == 0:
                    return False
            return True

        k = int(n ** 0.5)
        return (k ** 2 == n) and is_prime(k) and (k != 1)