from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = [0]
        ans = 0
        for i, h in enumerate(heights):
            while h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                ans = max(ans, height * width)
            stack.append(i)
        return ans
