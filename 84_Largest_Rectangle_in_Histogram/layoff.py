from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # add 哨兵 to the heights
        heights = [0] + heights + [0]
        res = 0
        stack = [0]
        for i in range(1, len(heights)):
            while heights[i] < heights[stack[-1]]:
                curr_height = heights[stack.pop()]
                curr_width = i - stack[-1] - 1
                res = max(res, curr_height*curr_width)
            stack.append(i)
        return res
