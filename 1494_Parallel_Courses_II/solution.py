import collections
import heapq


class Solution(object):
    def minNumberOfSemesters(self, n, dependencies, k):
        """
        :type n: int
        :type dependencies: List[List[int]]
        :type k: int
        :rtype: int
        """
        outgoing = collections.defaultdict(list)
        incoming = collections.defaultdict(int)
        for s, d in dependencies:
            incoming[d] += 1
            outgoing[s].append(d)
        queue = []
        for i in range(1, n+1):
            if i not in incoming:
                heapq.heappush(queue, (-len(outgoing[i]), i))
        ans = 0
        while queue:
            ans += 1
            limit = k
            l = len(queue)
            for _ in range(l):
                _, curr = heapq.heappop(queue)
                for nei in outgoing[curr]:
                    incoming[nei] -= 1
                    if incoming[nei] == 0:
                        heapq.heappush(queue, (-len(outgoing[nei]), nei))
                limit -= 1
                if limit == 0:
                    break

        return ans


print Solution().minNumberOfSemesters(4, [[2,1],[3,1],[1,4]], 2)
print Solution().minNumberOfSemesters(5, [[2,1],[3,1],[4,1],[1,5]], 2)
print Solution().minNumberOfSemesters(11, [], 2)
print Solution().minNumberOfSemesters(8,[[1,6],[2,7],[8,7],[2,5],[3,4]],3)
print Solution().minNumberOfSemesters(9,[[4,8],[3,6],[6,8],[7,6],[4,2],[4,1],[4,7],[3,7],[5,2],[5,9],[3,4],[6,9],[5,7]],2)
print Solution().minNumberOfSemesters(8, [[1,3],[1,4],[2,3],[2,4],[5,6],[6,7],[7,8]], 2)
print Solution().minNumberOfSemesters(8,[[2,7],[1,6],[2,8],[8,7],[6,7],[5,4],[1,7],[1,2],[1,4],[2,6]],3)