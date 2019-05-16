# -*- coding: utf-8 -*-
class Solution(object):
    def pushBoxes(self, caves, boxes):
        allow_height = float('inf')
        for i in range(len(caves)-1, -1, -1):
            allow_height = min(allow_height, caves[i])
            caves[i] = allow_height
        boxes.sort()
        count = 0
        pt1, pt2 = 0, 0
        while pt1 < len(caves) and pt2 < len(boxes):
            if caves[pt1] >= boxes[pt2]:
                count += 1
                pt1 += 1
                pt2 += 1
            else:
                pt1 += 1
                pt2 += 1
        return count

caves = [5, 10, 6]
boxes = [10, 30, 6, 5, 8, 7]

print Solution().pushBoxes(caves, boxes)
