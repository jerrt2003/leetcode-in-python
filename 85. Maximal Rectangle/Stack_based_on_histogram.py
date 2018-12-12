# -*- coding: utf-8 -*-
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        Solution: Stack + DP
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/maximal-rectangle/discuss/29065/AC-Python-DP-solutioin-120ms-based-on-largest-rectangle-in-histogram
        Algorithm:
        - Every row in the matrix is viewed as the ground with some buildings on it
        - Create a list: height
        - Create a area = 0
        - Scan through every row, when element is 1, than add 1 to height[i] otherwise height[i] = 0 (reset)
        - Once complete update list: height then we can use histogram algorithm to find max rectangle areas
            - create a list: stack and push [-1] into it
            - go through the list: height, if height[i] <= height[stack[-1]], then
                - h: height[stack.pop()]
                - w: i - stack[-1] -1
                - area = max(area, h*w)
                - push i into stack
            - when reached the end of stack, start to pop the stack to calculate all possible max rectangle
                - h: height[stack.pop()]
                - w: len(row) - stack[-1] -1
                - area = max(area, h*w)
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix is None or len(matrix) == 0:
            return 0
        len_heights = len(matrix[0])
        heights = [0 for _ in range(len_heights)]
        area = 0
        for row in matrix:
            for i in range(len_heights):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(len_heights):
                while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    area = max(area, h*w)
                stack.append(i)
            while stack[-1] != -1:
                h = heights[stack.pop()]
                w = len_heights - stack[-1] -1
                area = max(area,h*w)
        return area


input = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

sol = Solution()
print sol.maximalRectangle(input)