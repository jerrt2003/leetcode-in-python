# -*- coding: utf-8 -*-
class Solution(object):
    def findCircleNum(self, M):
        """
        Solution: DFS + Adjacent Matrix
        Time Complexity:
        Space Complexity:
        Inspired By:
        - https://www.geeksforgeeks.org/graph-and-its-representations/
        - https://leetcode.com/problems/friend-circles/solution/
        TP:
        - 原本以為這是個找island數目的題目 (e.g. LT_200: https://leetcode.com/problems/number-of-islands/)
        - 實際上這是一個adjacent matrix
        - use DFS to go through the matrix
        - since M is an adjacent matrix, so M is a square matrix with 對角線左上到右下為1 (自己跟自己一定是朋友)
        - create a self.visited to store visit node
            - every node will EVENTUALLY exist in self.visited since 他最起碼跟自己一定為朋友
        - When we hit i which is not in self.visited, means we haven't visit it yet, so start DFS against it
        :type M: List[List[int]]
        :rtype: int
        """
        self.M = M
        self.visited = list()
        count = 0
        for i in range(len(M)):
            if i not in self.visited:
                self.dfs(i)
                count += 1
        return count

    def dfs(self, i):
        for j in range(len(self.M)):
            if self.M[i][j] == 1 and j not in self.visited: # put visit node into self.visited
                self.visited.append(j)
                self.dfs(j)

M = [[1,1,0],
 [1,1,0],
 [0,0,1]]

sol = Solution()
print sol.findCircleNum(M)