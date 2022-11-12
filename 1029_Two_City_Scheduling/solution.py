class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        DFS
        T:O(2^n) S:O(1)
        TLE
        :type costs: List[List[int]]
        :rtype: int
        """
        self.min_cost = float('inf')
        def dfs(cost, lst, A, B):
            if A == 0 and B == 0:
                self.min_cost = min(cost, self.min_cost)
                return
            if A > 0:
                dfs(cost+lst[0][0], lst[1:], A-1, B)
            if B > 0:
                dfs(cost+lst[0][1], lst[1:], A, B-1)

        dfs(0, costs, len(costs)/2, len(costs)/2)
        return self.min_cost

print Solution().twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])
print Solution().twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])