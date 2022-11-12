# -*- coding: utf-8 -*-
import math
class Solution(object):
    def removeBoxes(self, boxes):
        """
        Solution: TLE and Not Correct !!
        :type boxes: List[int]
        :rtype: int
        """
        self.DP = dict()
        return int(self.findMax(boxes))

    def findMax(self, boxes):
        """
        to find maximum value
        :param boxes: a list of boxes
        :return: current max
        """
        if boxes is None or len(boxes) == 0: return 0
        if tuple(boxes) in self.DP: return self.DP[tuple(boxes)]
        curr_max = 0
        idx = 0
        while idx < len(boxes):
            start = end = idx
            while end < len(boxes) and boxes[start] == boxes[end]:
                end += 1
            idx = end
            next_boxes = boxes[:start] + boxes[end:]
            curr_max = max(curr_max, math.pow((end-start),2) + self.findMax(next_boxes))
        self.DP[tuple(boxes)] = curr_max
        return curr_max




#boxes = [1, 3, 2, 2, 2, 3, 4, 3, 1]
boxes = [3,8,8,5,5,3,9,2,4,4,6,5,8,4,8,6,9,6,2,8,6,4,1,9,5,3,10,5,3,3,9,8,8,6,5,3,7,4,9,6,3,9,4,3,5,10,7,6,10,7]
sol = Solution()
print sol.removeBoxes(boxes)