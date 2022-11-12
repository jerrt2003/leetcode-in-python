class Solution(object):
    def knapsack(self, w, v, W):
        """
        :type arr: List[int]
        :rtype: int
        """
        self.ans = -float('inf')
        l = len(w)
        def dfs(s, curr_w, curr_v):
            self.ans = max(self.ans, curr_v)
            if s == l:
                return
            for i in range(s, l):
                if curr_w + w[i] <= W:
                    dfs(i+1, curr_w+w[i], curr_v+v[i])

        dfs(0, 0, 0)
        return self.ans


print Solution().knapsack([10,20,30],[60,100,120],50)
print Solution().knapsack([1,1,2,2],[1,2,4,5],4)