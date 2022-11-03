class Solution:
    def heightChecker(self, heights):
        counts = [0] * (1 + max(heights))
        for h in heights:
            counts[h] += 1

        answer, idx = 0, 0
        for num in range(len(counts)):
            for _ in range(counts[num]):
                if num != heights[idx]:
                    answer += 1
                idx += 1
        return answer