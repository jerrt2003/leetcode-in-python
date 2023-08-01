import heapq
from typing import List


class Task:
    def __init__(self, idx, process_time):
        self.idx = idx
        self.process_time = process_time

    def __lt__(self, other):
        if self.process_time == other.process_time:
            return self.idx < other.idx
        return self.process_time < other.process_time


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks_with_idx = []
        for idx, task in enumerate(tasks):
            tasks_with_idx.append([idx, task[0], task[1]])

        # task: [idx, enqueue_time, process_time]
        tasks_with_idx.sort(key=lambda x: (x[1], x[2], x[0]))

        ans = []
        cur_time = 0
        pq = []

        while True:
            if len(ans) == len(tasks):
                break
            if len(pq) == 0:
                idx, enqueue_time, process_time = tasks_with_idx.pop(0)
                cur_time = enqueue_time
                heapq.heappush(pq, Task(idx, process_time))
            else:
                while pq:
                    cur_task = heapq.heappop(pq)
                    cur_time += cur_task.process_time
                    ans.append(cur_task.idx)

                    while tasks_with_idx and tasks_with_idx[0][1] <= cur_time:
                        idx, enqueue_time, process_time = tasks_with_idx.pop(0)
                        heapq.heappush(pq, Task(idx, process_time))

        return ans
