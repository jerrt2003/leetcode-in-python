from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        height = [0] + height
        stack = [0]
        ans = 0
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                low_idx = stack.pop()
                low = height[low_idx]
                if stack:
                    high = min(h, height[stack[-1]])
                    width = i - stack[-1] - 1
                    ans += width * (high - low)
            stack.append(i)
        return ans
