import heapq


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        Facebook
        Sort
        Heap
        Runtime: 56 ms, faster than 96.34% of Python online submissions for Meeting Rooms II.
        Memory Usage: 16.1 MB, less than 87.93% of Python online submissions for Meeting Rooms II.
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[0])
        pq = []
        for s, e in intervals:
            if not pq:
                heapq.heappush(pq, e)
            else:
                if s < pq[0]:
                    heapq.heappush(pq, e)
                else:
                    heapq.heappushpop(pq, e)
        return len(pq)
