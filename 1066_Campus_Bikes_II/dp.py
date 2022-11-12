import collections


class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        T:O(n) S:O(n)
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
        DP = collections.defaultdict(int)

        def dis(w, b):
            return abs(workers[w][0]-bikes[b][0]) + abs(workers[w][1]-bikes[b][1])


        def dfs(i, taken):
            if i == len(workers):
                return 0
            if taken in DP:
                return DP[taken]
            res = float('inf')
            for j in range(len(bikes)):
                if taken & (1 << j) == 0:
                    res = min(res, dis(i, j)+dfs(i+1, taken | (1 << j)))
            DP[taken] = res
            return DP[taken]

        return dfs(0, 0)

print Solution().assignBikes()

