__author__ = 'dcheng'
class Solution:
    def maxArea(self, height):
        """
        Solution: 2-pointer
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: MySELF!!
        TP:
        - Using 2 pointer to track
        :param height:
        :return:
        """
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