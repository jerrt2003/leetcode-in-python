import collections


class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        DFS
        T:O(n) S:O(n)
        Runtime: 1292 ms, faster than 94.99% of Python online submissions for Time Needed to Inform All Employees.
        Memory Usage: 50.6 MB, less than 100.00% of Python online submissions for Time Needed to Inform All Employees.
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        self.childs = collections.defaultdict(list)
        for i, v in enumerate(manager):
            if v == -1:
                continue
            self.childs[v].append(i)
        self.max_time = informTime[headID]

        def dfs(myChild, total_time):
            for child in myChild:
                if informTime[child] == 0:
                    self.max_time = max(self.max_time, total_time)
                    continue
                dfs(self.childs[child], total_time+informTime[child])

        dfs(self.childs[headID], informTime[headID])

        return self.max_time

# print Solution().numOfMinutes(1,0,[-1],[0])
# print Solution().numOfMinutes(6,2,[2,2,-1,2,2,2], [0,0,1,0,0,0])
print Solution().numOfMinutes(15,0,[-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6],[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0])