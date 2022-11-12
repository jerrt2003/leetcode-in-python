# -*- coding: utf-8 -*-
import heapq
class ExamRoom(object):
    def __init__(self, N):
        """
        Perf: Runtime: 72 ms, faster than 91.48% / Memory Usage: 12 MB, less than 54.13%
        :type N: int
        """
        self.N = N
        self.pq = [(self.dist(-1, N), -1, N)]

    def dist(self, i, j):
        if i == -1:
            return -j
        if j == self.N:
            return -(self.N-1-i)
        return -(abs(i-j)//2)

    def seat(self):
        """
        Time: log(n)
        :rtype: int
        """
        _, x, y = heapq.heappop(self.pq)
        if x == -1:
            seat = 0
        elif y == self.N:
            seat = self.N-1
        else:
            seat = (x+y)/2
        heapq.heappush(self.pq, (self.dist(x, seat), x, seat))
        heapq.heappush(self.pq, (self.dist(seat, y), seat, y))
        return seat

    def leave(self, p):
        """
        Time: O(n)
        :type p: int
        :rtype: None
        """
        head, tail = None, None
        for interval in self.pq:
            if interval[1] == p:
                tail = interval
            if interval[2] == p:
                head = interval
            if head and tail:
                break
        self.pq.remove(head)
        self.pq.remove(tail)
        heapq.heapify(self.pq)
        start, end = head[1], tail[2]
        heapq.heappush(self.pq, (self.dist(start, end), start, end))

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)