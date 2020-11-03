import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.q = []
        self.k = k
        for num in nums:
            heapq.heappush(self.q, num)
        while len(self.q) > self.k:
            heapq.heappop(self.q)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.q, val)
        if len(self.q) > self.k:
            heapq.heappop(self.q)
        return self.q[0]

# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(1, [])
param_1 = obj.add(-3)
param_1 = obj.add(-2)
param_1 = obj.add(-4)
param_1 = obj.add(0)
param_1 = obj.add(4)

