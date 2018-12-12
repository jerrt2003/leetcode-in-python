# -*- coding: utf-8 -*-
class Solution(object):
    def islandPerimeter(self, grid):
        """
        Solution: Hash
        Time Complexity:
        Space Complexity:
        Inspired By: MYSELF!!
        TP:
        - 每個island最多只有4面面海
        - create a list and use "how many faces facing the sea" as key, its value will be island's count
        - 然後我們針對每個island去算他有多少面面海,加到dict中
        - 最後k,v相乘, 相加即為答案
        :type grid: List[List[int]]
        :rtype: int
        """
        len_y = len(grid)
        len_x = len(grid[0])
        catogory = {}
        for y in range(len_y):
            for x in range(len_x):
                if grid[y][x] != 0:
                    k = 0
                    if x == 0 or grid[y][x-1] == 0: k+=1
                    if x == len_x-1 or grid[y][x+1] == 0: k+=1
                    if y == 0 or grid[y-1][x] == 0: k+=1
                    if y == len_y-1 or grid[y+1][x] == 0: k+=1
                    if catogory.has_key(k):
                        catogory[k] += 1
                    else:
                        catogory[k] = 1
        res = 0
        for k, v in catogory.iteritems():
            res += k*v
        return res

input = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
sol = Solution()
print sol.islandPerimeter(input)