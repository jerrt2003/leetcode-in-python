class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        Solution: Stack
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        Inspired By: https://leetcode.com/problems/exclusive-time-of-functions/discuss/105100/Python-Straightforward-with-Explanation
        TP:
        - To store "penalty time" in stack instead
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        res = [0 for _ in range(n)]
        for i in range(len(logs)):
            func, type, time = logs[i].split(':')
            func = int(func)
            time = int(time)
            if type == 'start':
                stack.append(time)
            else:
                delta = time - stack.pop() + 1
                res[func] = delta
                stack = [t+delta for t in stack]
        return res

n = 2
logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]

print Solution().exclusiveTime(n, logs)