# -*- coding: utf-8 -*-
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        Solution: BFS
        Time Complexity: O(mn)
        Space Complexity: O(2mn)
        Inspired By: https://leetcode.com/problems/walls-and-gates/discuss/72745/Java-BFS-Solution-O(mn)-Time
        TP:
        - Push all gates into queue first. Then for each gate update its neighbor cells and push them to the queue.
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]: return None
        m = len(rooms)
        n = len(rooms[0])
        q = []
        visited = set()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            curr = q.pop(0)
            curr_i, curr_j = curr[0], curr[1]
            for i, j in directions:
                x, y = curr_i+i, curr_j+j
                if 0 <= x < m and 0 <= y < n:
                    if rooms[x][y] != -1:
                        rooms[x][y] = min(rooms[x][y], 1+rooms[curr_i][curr_j])
                        if (x, y) not in visited: # !!! WHY we only keep on set of "visited": --> 若在本次循環中有個visited, 表示其他點已經捷足先登過了,換言之遮個visited的點距離其他門更近
                            q.append((x, y))
                            visited.add((x, y))
