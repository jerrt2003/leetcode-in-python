import heapq
from typing import List


class Event:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        if self.end == other.end:
            return self.start < other.start
        return self.end < other.end


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        ans = 0
        cur_time = 0
        pq = []
        while events:
            if len(pq) == 0:
                start, end = events.pop(0)
                heapq.heappush(pq, Event(start, end))
                cur_time = start
            while pq:
                next_event = heapq.heappop(pq)
                if cur_time <= next_event.end:
                    ans += 1
                    cur_time += 1
                    while events and events[0][0] <= cur_time:
                        _s, _e = events.pop(0)
                        heapq.heappush(pq, Event(_s, _e))
        return ans
