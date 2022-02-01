import heapq


class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.nums = sorted(nums, reverse=True)[:k]
        heapq.heapify(self.nums)

    def add(self, val):
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
