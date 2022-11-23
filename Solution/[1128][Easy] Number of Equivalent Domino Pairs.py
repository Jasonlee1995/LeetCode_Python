class Solution:
    def numEquivDominoPairs(self, dominoes):
        count = {}
        for a, b in dominoes:
            a, b = min(a, b), max(a, b)
            if (a, b) not in count: count[(a, b)] = 0
            count[(a, b)] += 1

        answer = 0
        for key in count:
            if count[key] > 1:
                n = count[key]
                answer += (n * (n-1)) // 2
        return answer