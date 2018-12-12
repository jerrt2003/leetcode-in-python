# -*- coding: utf-8 -*-
# Definition for a point.
import json
from decimal import *
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        Solution: Hashtable + "SLOPE"
        Time Complexity: O(n^2)
        Space Complexity:
        Inspired By: https://leetcode.com/problems/max-points-on-a-line/discuss/47117/Sharing-my-simple-solution-with-explanation
        Thinking Process:
        - Basic idea: Use any point on the map as starting point, how to find any pair of 2 points (A, other_point)
        are at same line..?
            - USING SLOPE(斜率)
            - Ex. (A, B)'s slope == (A, C)'s slope -> A, B, C are at same line
            - 3 situation we might face during the calculation
                - the other point might be at same location as A --> we still need to count it
                - A's x axis are same as other point's x axis --> slope is infinite (x座標相同,斜率無限大) (!! no need to check y axis is same condition is its slope is 0 which will be covered by general case)
                - General case: compute slope between A and other point and using slope value to store in the map (if k/v already exist then +1)
                - Once go through all case between A and other points, we find the slope with maximum number(max_num)
                - Then we add same_location_value to max_num
                - Update global max_num
                - Repeat the same logic to other point
                - Return the max_num
                - !! Consider Precision Case: USE float datatypes or even decimal(by default 精確到28位)
        :type points: List[Point]
        :rtype: int
        """
        max_nums_points = 0
        n = len(points)
        for i in range(n):
            same_point_count = 1
            slope_map = {}
            for j in range(i + 1, n):
                # case 1: same point
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    same_point_count += 1
                # case 2: slope is INF
                elif points[i].x == points[j].x:
                    try:
                        slope_map['inf'] += 1
                    except:
                        slope_map['inf'] = 1
                # case 3: general
                else:
                    slope = Decimal((points[i].y - points[j].y)) / Decimal(points[i].x - points[j].x)
                    try:
                        slope_map[slope] += 1
                    except:
                        slope_map[slope] = 1
            if slope_map:
                local_max_counts = max(slope_map.values())
                local_max_counts += same_point_count
            else:
                local_max_counts = same_point_count
            max_nums_points = max(max_nums_points, local_max_counts)
        return max_nums_points


def stringToPoint(input):
    tokens = json.loads(input)
    return Point(tokens[0], tokens[1])


def stringToPointArray(input):
    pointArrays = json.loads(input)
    points = []
    for pointArray in pointArrays:
        points.append(stringToPoint(json.dumps(pointArray)))
    return points


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    #input = '[[84,250],[0,0],[1,0],[0,-70],[0,-70],[1,-1],[21,10],[42,90],[-42,-230]]'
    input = '[[0,0],[94911151,94911150],[94911152,94911151]]'

    points = stringToPointArray(input)

    ret = Solution().maxPoints(points)

    out = intToString(ret)
    print out



if __name__ == '__main__':
    main()