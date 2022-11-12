import collections


class Solution(object):
    def shortestWay(self, source, target):
        """
        BS
        T:nlog(m) S:O(m)
        Runtime: 32 ms, faster than 66.02% of Python online submissions for Shortest Way to Form String.
        Memory Usage: 12.9 MB, less than 100.00% of Python online submissions for Shortest Way to Form String.
        :type source: str
        :type target: str
        :rtype: int
        """
        def bs(lst, idx):
            l, r = 0, len(lst)
            while l < r:
                m = (l+r-1)/2
                if lst[m] > idx:
                    r = m
                else:
                    l = m+1
            return l


        graph = collections.defaultdict(list)
        for i, v in enumerate(source):
            graph[v].append(i)

        last_idx = -1
        count = 1
        for c in target:
            if c not in graph:
                return -1
            pos = bs(graph[c], last_idx)
            if pos == len(graph[c]):
                count += 1
                last_idx = graph[c][0]
            else:
                last_idx = graph[c][pos]
        return count

print Solution().shortestWay('abc','abcbc')