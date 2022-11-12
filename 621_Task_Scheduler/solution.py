import heapq
import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        Facebook
        Heapq
        T:O(nlogn) S:O(n)
        Runtime: 1252 ms, faster than 5.05% of Python online submissions for Task Scheduler.
        Memory Usage: 14.7 MB, less than 95.17% of Python online submissions for Task Scheduler.
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        h = []
        counter = collections.Counter(tasks)
        ans = 0
        for k, v in counter.iteritems():
            heapq.heappush(h, (-v, k))
        while h:
            i, nxt_avai = 0, []
            while i <= n:
                ans += 1
                if h:
                    v, k = heapq.heappop(h)
                    if v != -1:
                        nxt_avai.append((v+1, k))
                if not h and not nxt_avai:
                    break
                else:
                    i += 1
            if nxt_avai:
                for v, k in nxt_avai:
                    heapq.heappush(h, (v, k))
        return ans


print Solution().leastInterval(["A","A","A","B","B","B"], 2)
print Solution().leastInterval(["A","A","A","B","B","B"], 0)
print Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],2)