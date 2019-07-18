# -*- coding: utf-8 -*-
class Solution(object):
    def dailyTemperatures(self, T):
        """
        T:O(n)
        S:O(n)
        Perf: Runtime: 420 ms, faster than 98.62% / Memory Usage: 15.1 MB, less than 59.41%
        :type T: List[int]
        :rtype: List[int]
        """
        res = [0]*len(T)
        stack = []
        for i, temp in enumerate(T):
            if not stack:
                stack.append(i)
            else:
                while stack and temp > T[stack[-1]]:
                    idx = stack.pop()
                    res[idx] = i - idx
                stack.append(i)
        return res

assert Solution().dailyTemperatures([73,74,75,71,69,72,76,73]) == [1, 1, 4, 2, 1, 1, 0, 0]