# -*- coding: utf-8 -*-
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        Stack Solution
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/largest-rectangle-in-histogram/solution/
        算法：
        1. Create a stack and push '-1' into stack (為什麼需要push -1: 因為符合待會算寬度的邏輯)
        2. initial area = 0
        3. Go through the heights list and do following:
        - if heights[i] > heights[stack[-1] (e.g. 現存stack中heights最高者), continue to push idx i into stack (升冪)
        - when heights[i] <= heights[stack[-1]]: 一旦遇到降冪, 則可以開始往前算面積
            - h = heights[stack.pop()]
            - w = i - stack[-1] - 1 (算寬度)
            - area = max(area, h*w)
            - 一直算到 heights[i] >= heights[stack[-1]] 為止
            - 跳出while loop後要記得把current i push進去stack
        - when reached the end of list, then start pop the stack till stack reached -1 (e.g. 開始算所有剩下有可能的面積)
            - h = heights[stack.pop()]
            - w = len(heights) - stack[-1] -1
            - area = max(area, h*w)
        - (最後留下來的長方圖應為一個升冪排序的長方圖)
        :type heights: List[int]
        :rtype: int
        """

        len_heights = len(heights)
        stack = [-1]
        area = 0
        for i in range(len_heights):
            while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                area = max(area, h*w)
            stack.append(i)
        while stack[-1] != -1:
            h = heights[stack.pop()]
            w = len_heights - stack[-1] -1
            area = max(area, h*w)
        return area

#histogram = [2,1,5,6,2,3]
histogram = [6, 7, 5, 2, 4, 5, 9, 3]
sol = Solution()
print sol.largestRectangleArea(histogram)
