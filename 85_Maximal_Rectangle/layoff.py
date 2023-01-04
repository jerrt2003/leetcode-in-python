from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ans = 0
        if not matrix:
            return 0
        heights: List[int] = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            ans = max(ans, self.maxHistogram(heights))
        return ans

    def maxHistogram(self, heights: List[int]) -> int:
        """to return a maxmimum histogram areas based on
        given heights information

        Args:
            heights (List[int]): list of heights

        Returns:
            int: maxmimum areas
        """
        heights = [0] + heights + [0]
        stack = [0]
        ret = 0
        for i in range(1, len(heights)):
            while heights[i] < heights[stack[-1]]:
                curr_height = heights[stack.pop()]
                curr_width = i - stack[-1] -1
                ret = max(ret, curr_height*curr_width)
            stack.append(i)
        return ret
