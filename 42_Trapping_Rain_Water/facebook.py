class Solution(object):
    def trap(self, height):
        """
        Facebook
        Stack + Mono-Q
        T:O(n) S:O(n)
        Runtime: 36 ms, faster than 86.38% of Python online submissions for Trapping Rain Water.
        Memory Usage: 13.2 MB, less than 75.00% of Python online submissions for Trapping Rain Water.
        :type height: List[int]
        :rtype: int
        """
        # stack = []
        # ans = 0
        # for i, h in enumerate(height):
        #     if not stack or h < height[stack[-1]]:
        #         stack.append(i)
        #     else:
        #         while h > height[stack[-1]]:
        #             low = height[stack.pop()]
        #             if not stack:
        #                 break
        #             _w = i - stack[-1] - 1
        #             _h = min(h, height[stack[-1]]) - low
        #             ans += _w * _h
        #         stack.append(i)
        # return ans
        stack = []
        ans = 0
        for i, h in enumerate(height):
            if not stack or h <= height[stack[-1]]:
                stack.append(i)
            else:
                while height[stack[-1]] < h:
                    low = height[stack.pop()]
                    if not stack:
                        break
                    high = min(h, height[stack[-1]])
                    h = high - low
                    w = i - stack[-1] - 1
                    ans += h*w
                stack.append(i)
        return ans

