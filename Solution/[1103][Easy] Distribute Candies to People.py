class Solution:
    def distributeCandies(self, candies, num_people):
        n = num_people
        num_sum = n * (n+1) // 2
        l = 0
        cnt = lambda x: (num_sum * (x+1)) + (n ** 2) * (x * (x+1) // 2)
        while candies >= cnt(l):
            l += 1
        get = cnt(l) - candies
        answer = [i * (l+1) + n * (l * (l+1) // 2) for i in range(1, n+1)]
        for i in range(n-1, -1, -1):
            candy = 1 + i + n * l
            if get < candy:
                answer[i] -= get
                break
            else:
                answer[i] -= candy
                get -= candy
        return answer