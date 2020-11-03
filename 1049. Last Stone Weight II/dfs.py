class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        self.ans = float('inf')
        stones.sort()
        self.visit = set()

        def dfs(stones):
            if tuple(stones) in self.visit:
                return
            self.visit.add(tuple(stones))
            if len(stones) == 0:
                self.ans = 0
            elif len(stones) == 1:
                self.ans = min(self.ans, stones[0])
            else:
                for i in range(1, len(stones)):
                    next_stones = sorted(stones[1:i]+stones[i+1:]+[stones[i]-stones[0]])
                    dfs(next_stones)

        dfs(stones)
        return self.ans


print Solution().lastStoneWeightII([2,7,4,1,8,1])