import collections


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        Facebook
        T:O(n) S:O(n)
        Runtime: 548 ms, faster than 50.76% of Python online submissions for Task Scheduler.
        Memory Usage: 14.7 MB, less than 78.86% of Python online submissions for Task Scheduler.
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = collections.Counter(tasks)
        M = max(counter.values())
        Mct = counter.values().count(M)
        return max(len(tasks), (M - 1) * (n + 1) + Mct)
