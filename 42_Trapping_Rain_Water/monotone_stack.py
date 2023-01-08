from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        # 加入哨兵
        height = [0] + height + [0]
        stack = [0]
        for i in range(1, len(height)):
            while stack and height[i] > height[stack[-1]]:
                min_height = height[stack.pop()]
                if stack:
                    curr_height = min(height[stack[-1]], height[i]) - min_height
                    curr_width = i - stack[-1] - 1
                    ans += curr_height * curr_width
            stack.append(i)
        return ans
