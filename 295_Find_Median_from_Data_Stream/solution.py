import heapq

from typing import List

class PriorityQueue():
    def __init__(self, isMin: bool = True):
        self.queue: List[int] = []
        self.isMin = isMin
        heapq.heapify(self.queue)
    
    def peak(self):
        return self.queue[0] if self.isMin else -1 * self.queue[0]

    def push(self, num: int):
        if self.isMin:
            heapq.heappush(self.queue, num)
        else:
            heapq.heappush(self.queue, -1 * num)

    def pop(self) -> int:
        pop_num = heapq.heappop(self.queue)
        return pop_num if self.isMin else -1 * pop_num

    def get_len(self) -> int:
        return len(self.queue)

class MedianFinder:

    def __init__(self):
        self.l = PriorityQueue(isMin=False) # left queue is max-heap
        self.r = PriorityQueue() # right queue is min-heap

    def addNum(self, num: int) -> None:
        # if l size == r size
        if self.l.get_len() == self.r.get_len():
            if self.r.get_len() == 0: # if both queue empty, push to left
                self.l.push(num)
            else:
                if num > self.r.peak(): # ex. l=[3], r=[3], num = 4 -> l=[3,3], r=[4]
                    self.l.push(self.r.pop())
                    self.r.push(num)
                else:
                    self.l.push(num)
        else:
            if num >= self.l.peak(): # l=[2,3] r=[4], num=4 -> l=[2,3], r=[3,4]
                self.r.push(num)
            else:
                self.r.push(self.l.pop())
                self.l.push(num)


    def findMedian(self) -> float:
        if self.l.get_len() == self.r.get_len():
            l_top, r_top = self.l.peak(), self.r.peak()
            return (l_top+r_top)/2
        else:
            return self.l.peak()

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()