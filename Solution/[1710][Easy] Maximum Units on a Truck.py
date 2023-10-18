class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x: -x[1])
        answer = 0
        for box, units in boxTypes:
            if truckSize > box:
                truckSize -= box
                answer += box * units
            else:
                answer += truckSize * units
                break
        return answer