import heapq

from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        pq: List[int] = []
        heapq.heapify(pq)
        for s, e in intervals:
            if len(pq) == 0:
                heapq.heappush(pq, e)
            else:
                if s < pq[0]:
                    heapq.heappush(pq, e)
                else:
                    heapq.heappushpop(pq, e)
        return len(pq)