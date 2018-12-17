# -*- coding: utf-8 -*-
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        res = [0 for _ in range(n)]
        i = 1
        while i < len(logs):
            curr_func, curr_type, curr_ts = logs[i].split(':')
            prev_func, prev_type, prev_ts = logs[i-1].split(':')
            interval = int(curr_ts) - int(prev_ts)
            if curr_func == prev_func:
                res[int(curr_func)] += interval+1
            elif curr_type == prev_type == 'start':
                stack.append([prev_func, interval])
            elif curr_type == 'start' and prev_type == 'end':
                stack.append([curr_func, interval])
            elif curr_type == prev_type == 'end':
                last_func, last_interval = stack.pop()
                total_interval = last_interval + interval
                res[int(last_func)] += total_interval
            i += 1
        return res

n = 3
logs = ["0:start:0","1:start:2","1:end:5","2:start:6","2:end:14","0:end:15"]

print Solution().exclusiveTime(n, logs)