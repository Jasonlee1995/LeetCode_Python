import heapq


class Solution:
    def lastStoneWeight(self, stones):
        h = [-stone for stone in stones]
        heapq.heapify(h)
        while len(h) > 1:
            heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
        return -h[0]