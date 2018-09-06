__author__ = 'dcheng'
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        if len(height) == 0:
            return -1
        left = 0
        right = len(height) - 1
        maxWater = 0
        while left < right:
            maxWater = max(maxWater, (right-left)*min(height[left],height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxWater