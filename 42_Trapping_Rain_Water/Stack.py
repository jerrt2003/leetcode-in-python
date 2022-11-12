# -*- coding: utf-8 -*-
class Solution(object):
    def trap(self, height):
        """
        Solution: Stack
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: https://leetcode.com/problems/trapping-rain-water/discuss/17414/A-stack-based-solution-for-reference-inspired-by-Histogram
        TP:
        - Very similar to the Q.84 (histogram)
        - 升冪/降冪
        - First how we decide how much water we can trap?
            - use current height as bottom, left higher bar as left_h, right higher bar as right_h
            - then we compute width: w (more on this later)
            - total water will be (min(left_h, right_h) - bottom) * w
        - ok so now we have basic idea how to calculate water, we can develop our algorithm:
            - create a stack: stack = list()
            - go through the height list
            - if current height (height[i]) is small or equal to previous height (height[stack[-1]] then we append i into stack (降冪)
            - if not which means we find the right height which can trap the water, so we start to compute the max water
                - use current height[i] as right height: right_h
                - use height[stack.pop()] as bottom: bottom
                - use previous high bar: height[stack[-1]] as left height: left_h
                - so we can have h = min(left_h, right_h) - bottom
                - now we can compute the width which will be: i - left - 1
                    - WHY ?? 因為我們在每次計算時是計算以bottom為底的儲水量, 比bottom高一階的水會在下一個循環中被算到
                - So maxWater += h*w
                - Continue this cycle till height[i] < stack[-1] (升冪)
                - Push current i into stack before moving forward
            - return maxWater
        :type height: List[int]
        :rtype: int
        """
        if height is None: return 0
        stack = list()
        maxWater = 0
        for i in range(len(height)):
            if len(stack) == 0 or height[i] <= height[stack[-1]]:
                stack.append(i)
            else:
                while height[i] > height[stack[-1]]:
                    right_height = height[i]
                    bottom_height = height[stack.pop()]
                    if len(stack) == 0: # boundary condition, when there is no left barrier
                        break
                    left_height = height[stack[-1]]
                    h = min(right_height, left_height) - bottom_height
                    # Consider this: [5,4,2,1,1,3]
                    # when we hit i = 5, the r_height is 3, bottom_height is height[stack.pop()] = 1, the left_height will be height[stack[-1]] = 1
                    # so we have a situation of: h = min(r_height, l_height) - bottom_height = 1 - 1 = 0
                    # thus water we calculate during this iteration will be: w * h = (5-3-1) * 0 = 0
                    # but that's ok, since next iteration we will calculate the real water trap between i = 2 ~ i = 5
                    w = i - stack[-1] - 1
                    maxWater += h*w
                stack.append(i)
        return maxWater

height = [0,1,0,2,1,0,1,3,2,1,2,1]
sol = Solution()
print sol.trap(height)
