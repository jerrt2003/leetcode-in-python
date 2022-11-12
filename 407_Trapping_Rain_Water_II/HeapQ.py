# -*- coding: utf-8 -*-
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        Solution: Heap (Priority Q)
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        Inspired By:
        - https://leetcode.com/problems/trapping-rain-water-ii/discuss/89466/python-solution-with-heap
        - https://www.youtube.com/watch?time_continue=7&v=cJayBq38VYw
        TP:
        - first we have to define "how to trap a water"
            - since all border can't "trap" any water, we can put all border elements into the heapQ
        - The we go through the following procedure:
            - pop from heapQ (the pop will give us lowest height cell)
            - visit all its 'unvisited neighbor'
                - if neighbor's height is smaller than 'pop' height, means we can trap water, so add the height diff to res
                - then we push this neighbor into heap
                    - !!! Tricky: we need to update this neighbor's height with max(height_of_neighbor, height_pop)
                    - WHY ?? --> if neighbor's height is smaller, then we already add the 'trap' water during this iteration
                        thus next time when its 'neighbor' turn from heapQ we can have correct amount of water
                    - consider this:
                        5 7 3 <-- current pop is 7
                        4 6 1 <-- visit neighbor 6, collect water 7-6 = 1, push 6 with height of 7 into heap
                        6 5 7 <-- next time when pop 6 and visit neighbor 5, neighbor should able to trap water 7 - 5 = 2
                        7 7 8
        - Since we start from lowest point from all borders, we can guarantee for following procedure the water will be trapped correctly
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]: return 0
        import pq
        m = len(heightMap)
        n = len(heightMap[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        res = 0
        heap = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    pq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        while heap:
            height, i, j = pq.heappop(heap)
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    res += max(0, height - heightMap[x][y])
                    pq.heappush(heap, (max(heightMap[x][y], height), x, y))
                    visited[x][y] = True

        return res