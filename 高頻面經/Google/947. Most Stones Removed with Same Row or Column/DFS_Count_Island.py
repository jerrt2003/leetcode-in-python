# -*- coding: utf-8 -*-
import hash2
class Solution(object):
    def removeStones(self, stones):
        """
        Solution: DFS + Count Island
        Time Complexity:
        Space Complexity: O(2n)
        Inspired By: (92ms, beat 46.64%)
        - https://www.jianshu.com/p/30d2058db7f7
        - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/discuss/197668/Count-the-Number-of-Islands-O(N)
        TP:
        - Connected stones can be reduced to 1 stone, the maximum stones can be removed = stones number - islands number.
          so just count the number of "islands".
        - 如果两个石头在同行或者同列，两个石头就是连接的。连在一起的石头，可以组成一个连通图。每一个连通图至少会剩下1个石头。
          所以我们希望存在一种思路，每个连通图都只剩下1个石头。这样这题就转化成了数岛屿的问题。
        :type stones: List[List[int]]
        :rtype: int
        """
        '''
        row_set = collections.defaultdict(set)
        col_set = collections.defaultdict(set)
        for i, j in stones:
            row_set[i].add(j)
            col_set[j].add(i)

        def DFS_Row(i):
            seen_row.add(i)
            for j in row_set[i]:
                if j not in seen_col:
                    DFS_Col(j)

        def DFS_Col(j):
            seen_col.add(j)
            for i in col_set[j]:
                if i not in seen_row:
                    DFS_Row(i)

        seen_row = set()
        seen_col = set()
        island = 0
        for i, j in stones:
            if i not in seen_row:
                island += 1
                DFS_Row(i)
                DFS_Col(j)

        return len(stones) - island
        '''
        # refine version
        stone_set = hash2.defaultdict(set)
        for i, j in stones:
            stone_set[i].add(~j)
            stone_set[~j].add(i) # inverse j to make sure j will not collide with i in stone_set

        def DFS(i):
            seen.add(i)
            for elem in stone_set[i]:
                if elem not in seen:
                    DFS(elem)

        seen = set()
        island = 0
        for i, j in stones:
            if i not in seen:
                island += 1
                DFS(i)
                DFS(~j)

        return len(stones) - island

stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
print Solution().removeStones(stones)