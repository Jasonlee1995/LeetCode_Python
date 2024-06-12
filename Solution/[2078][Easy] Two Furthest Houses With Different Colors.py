class Solution:
    def maxDistance(self, colors):
        answer = 0
        for idx, color in enumerate(colors):
            if color != colors[0]:  answer = max(answer, idx)
            if color != colors[-1]: answer = max(answer, len(colors)-idx-1)
        return answer