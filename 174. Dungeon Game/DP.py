# -*- coding: utf-8 -*-
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        Solution: DP
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        Perf: Runtime: 32 ms, faster than 66.15% / Memory Usage: 11.7 MB, less than 15.38%
        Inspired By:
        - https://leetcode.com/problems/dungeon-game/discuss/52774/C++-DP-solution
        - https://leetcode.com/problems/dungeon-game/discuss/52774/C++-DP-solution/53800
        TP:
        - reverse thinking: traverse from bottom-right to top-left
        - each DP[i][j] represent min-health need to be in order to arrive dungeon[i][j]
        - So it may lead to 2 situation:
            - if dungeon[i][j] <= 0, then we just need to find min(DP[i][j+1], DP[i+1[j]) - dungeon[i][j] to find the min-health
            - however dungeon may > 0, then min-health will need to be 1 to arrive this cell (health = 0 is dead)
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if dungeon is None or len(dungeon) == 0:
            return None

        row = len(dungeon)
        col = len(dungeon[0])
        DP = [[float('inf') for _ in range(col+1)] for _ in range(row+1)]

        DP[row][col-1] = 1 # !! need to initialize so we can get correct DP[row][col] as starting DP
        DP[row-1][col] = 1

        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                DP[i][j] = max(min(DP[i][j+1], DP[i+1][j])-dungeon[i][j],1)

        return DP[0][0]



dungeon = [[-2,-3,3],
          [-5,-10,1],
          [10,30,-5]]

#dungeon = [[100]]

#dungeon = [[0, -3]]


print Solution().calculateMinimumHP(dungeon)