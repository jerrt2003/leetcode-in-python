# -*- coding: utf-8 -*-
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        Solution: Stack (Better Version)
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: https://leetcode.com/problems/exclusive-time-of-functions/discuss/105072/Python-Stack-Solution
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0 for _ in range(n)]
        stack = []
        for log in logs:
            func, type, time = log.split(':')
            func = int(func)
            time = int(time)
            if type == 'start':
                stack.append([time, 0]) # data_structure: [start_time, penalty_time] (only func_type == 'start' will push into stack thus I call it as start_time)
            else:
                start_time, penalty_time = stack.pop()
                res[func] = time - start_time - penalty_time + 1
                if stack:
                    '''
                    Just need to count the total exec. time of this function and add it to prev. func penalty time
                    ex. "0:start:0", "1:start:2", "1:end:5", "2:start:6", "2:end:8", "0:end:9"
                    stack status: 
                    [[0,0]] (append)
                    [[0,0],[1,0]] (append)
                    [[0,4]] (pop) (why..? cuz func 1 total exec time is 5-2+1 = 4 so we add 4 into func 0's penalty time
                    [[0,4],[2,0]] (append)
                    [[0,7]] (pop) (why..? cuz func 2 total exec time is 8-6+1 = 3 so we add 3 into func 0's penalty time again.
                    So func 0's total exec time will be:
                    9 - 0 - 7 + 1 = 3            
                    '''
                    stack[-1][1] += time - start_time + 1
        return res

n = 2
logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]

print Solution().exclusiveTime(n, logs)