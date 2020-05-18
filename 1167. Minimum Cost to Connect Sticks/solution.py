import heapq

class Solution(object):
    def connectSticks(self, sticks):
        """
        Heap
        T:O(nlogn) S:O(n)
        Runtime: 792 ms, faster than 89.98% of Python online submissions for Minimum Cost to Connect Sticks.
        Memory Usage: 13.4 MB, less than 100.00% of Python online submissions for Minimum Cost to Connect Sticks.
        :type sticks: List[int]
        :rtype: int
        """
        # pq = []
        # for s in sticks:
        #     heapq.heappush(pq, s)
        heapq.heapify(sticks)
        
        cost = 0
        while len(sticks) > 1:
            s1 = heapq.heappop(sticks)
            s2 = heapq.heappop(sticks)
            _cost = s1 + s2
            cost += _cost
            heapq.heappush(sticks, _cost)
        
        return cost

print Solution().connectSticks([2,4,3])
print Solution().connectSticks([1,8,3,5])

