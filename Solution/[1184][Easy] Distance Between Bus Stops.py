class Solution:
    def distanceBetweenBusStops(self, distance, start, destination):
        start, destination = min(start, destination), max(start, destination)
        total = sum(distance)
        cw = sum(distance[start:destination])
        ccw = total - cw
        return min(cw, ccw)