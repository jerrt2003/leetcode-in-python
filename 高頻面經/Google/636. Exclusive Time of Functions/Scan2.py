# -*- coding: utf-8 -*-
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        T:O(n)
        S:O(n)
        Perf: Runtime: 68 ms, faster than 83.66% / Memory Usage: 11.8 MB, less than 72.45%
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0]*n
        stack = []
        for log in logs:
            id, ops, ts = log.split(':')
            id = int(id)
            ts = int(ts)
            if ops == 'start':
                stack.append([ts, 0])
            else:
                start_ts, penalty = stack.pop()
                res[id] += (ts - start_ts - penalty + 1)
                if stack:
                    stack[-1][1] += (ts - start_ts + 1)
        return res