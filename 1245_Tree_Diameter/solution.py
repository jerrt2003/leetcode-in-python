import collections


class Solution(object):
    def treeDiameter(self, edges):
        """
        BFS
        LC.310
        T:O(n) S:O(n)
        Runtime: 164 ms, faster than 59.13% of Python online submissions for Tree Diameter.
        Memory Usage: 17.1 MB, less than 100.00% of Python online submissions for Tree Diameter.
        :type edges: List[List[int]]
        :rtype: int
        """
        self.graph = collections.defaultdict(list)
        for s, e in edges:
            self.graph[s].append(e)
            self.graph[e].append(s)
        queue = [a for a in self.graph if len(self.graph[a]) == 1]
        ret = 0
        while len(queue) > 1:
            ret += 2
            nxtQueue = []
            for i in range(len(queue)):
                j = queue.pop()
                for neigh in self.graph[j]:
                    self.graph[neigh].remove(j)
                    if len(self.graph[neigh]) == 1:
                        nxtQueue.append(neigh)
            queue = nxtQueue
        return ret-1 if len(queue) == 0 else ret


print Solution().treeDiameter([[0,1],[0,2]])