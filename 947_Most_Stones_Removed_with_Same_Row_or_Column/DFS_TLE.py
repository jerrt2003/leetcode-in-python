# -*- coding: utf-8 -*-
import collections
import copy
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        row_stone = collections.defaultdict(list)
        col_stone = collections.defaultdict(list)
        for x, y in stones:
            row_stone[x].append(y)
            col_stone[y].append(x)
        self.res = 0
        self.DFS(stones, row_stone, col_stone, 0)
        return self.res

    def DFS(self, stones, row_stone, col_stone, stone_removed):
        if len(stones) == 0:
            return
        for i in range(len(stones)):
            x, y = stones[i]
            if len(row_stone[x]) > 1 or len(col_stone[y]) > 1:
                self.res = max(self.res, stone_removed+1)
                next_stones = stones[:]
                next_stones.pop(i)
                next_row_stone = copy.deepcopy(row_stone)
                next_row_stone[x].remove(y)
                next_col_stone = copy.deepcopy(col_stone)
                next_col_stone[y].remove(x)
                self.DFS(next_stones, next_row_stone, next_col_stone, stone_removed+1)


stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2],[3,1]]
print Solution().removeStones(stones)

