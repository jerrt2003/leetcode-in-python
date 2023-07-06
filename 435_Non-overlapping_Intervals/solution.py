import collections
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        remove = 0
        stack = collections.deque()

        for [s, e] in intervals:
            if not stack:
                stack.append([s, e])
            else:
                [_, prev_e] = stack[-1]
                if s < prev_e:
                    remove += 1
                else:
                    stack.append([s, e])

        return remove
