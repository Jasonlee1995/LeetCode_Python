class Solution:
    def busyStudent(self, startTime, endTime, queryTime):
        return sum(st <= queryTime <= et for st, et in zip(startTime, endTime))