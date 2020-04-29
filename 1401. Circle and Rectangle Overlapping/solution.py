import math
class Solution(object):
    # def checkOverlap(self, radius, x_center, y_center, x1, y1, x2, y2):
    #     """
    #     Navice Solution
    #     :type radius: int
    #     :type x_center: int
    #     :type y_center: int
    #     :type x1: int
    #     :type y1: int
    #     :type x2: int
    #     :type y2: int
    #     :rtype: bool
    #     """
    #     def isOverlap(radius, len_x, len_y):
    #         l = math.sqrt(pow(len_x, 2)+pow(len_y, 2))
    #         return l <= radius
    #
    #     if x_center in range(x1, x2+1) and y_center in range(y1, y2+1):
    #         return True
    #
    #     for i in range(x1, x2+1):
    #         if isOverlap(radius, i-x_center, y1-y_center) or isOverlap(radius, i-x_center, y2-y_center):
    #             return True
    #
    #     for j in range(y1, y2+1):
    #         if isOverlap(radius, x1-x_center, j-y_center) or isOverlap(radius, x2-x_center, j-y_center):
    #             return True
    #
    #     return False
    def checkOverlap(self, radius, x_center, y_center, x1, y1, x2, y2):
        """
        find the closest point
        T:O(1) S:O(1)
        Runtime: 20 ms, faster than 54.90% of Python online submissions for Circle and Rectangle Overlapping.
        Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for Circle and Rectangle Overlapping.
        :type radius: int
        :type x_center: int
        :type y_center: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        x_nearst = max(x1, min(x_center, x2))
        y_nearst = max(y1, min(y_center, y2))

        return (x_nearst-x_center)*(x_nearst-x_center)+(y_nearst-y_center)*(y_nearst-y_center) <= radius*radius



print Solution().checkOverlap(1,0,0,1,-1,3,1)
print Solution().checkOverlap(1,0,0,-1,0,0,1)
print Solution().checkOverlap(1,1,1,-3,-3,3,3)
print Solution().checkOverlap(1,1,1,1,-3,2,-1)