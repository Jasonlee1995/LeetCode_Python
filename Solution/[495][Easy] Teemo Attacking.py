class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        answer = duration
        for i in range(len(timeSeries)-1):
            answer += min(timeSeries[i+1] - timeSeries[i], duration)
        return answer
