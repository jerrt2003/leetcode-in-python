# -*- coding: utf-8 -*-
import collections
import heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        Solution: Calculating Idle Slot
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MySELF!! (684ms, beat 20.24%)
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq2task_map = collections.Counter(tasks)
        max_freq = max(freq2task_map.values())
        base_sec = []
        for k, v in freq2task_map.iteritems():
            if v == max_freq:
                base_sec.append(k)
        for key in base_sec:
            freq2task_map.pop(key)

        res = len(base_sec)

        _heap = []
        for i in range(max_freq-1):
            heapq.heappush(_heap, (len(base_sec), base_sec[:]))
        freq2task_map = [(k, v) for k, v in freq2task_map.iteritems()]
        while freq2task_map:
            k, v = freq2task_map.pop()
            for i in range(v):
                sec_len, sec = heapq.heappop(_heap)
                sec.append(k)
                heapq.heappush(_heap, (1+sec_len, sec))
        while _heap:
            sec_len, sec = _heap.pop()
            res += max(n+1, sec_len)
        return res



tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print Solution().leastInterval(tasks, n)





