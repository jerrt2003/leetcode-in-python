# -*- coding: utf-8 -*-
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        Solution: O(n)
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: https://leetcode.com/problems/heaters/discuss/95878/10-lines-python-with-easy-understanding
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        heaters = [-float('inf')] + heaters + [float('inf')] # !!!!!!
        res, i = 0, 0
        for house in houses:
            while house > heaters[i+1]:
                i += 1
            _min_radius = min(house-heaters[i], heaters[i+1]-house)
            res = max(res, _min_radius)
        return res

#houses = [1,2,3]
#heaters = [2]

#houses = [1,2,3,4]
#heaters = [1,4]

houses = [1,2,3,5,15]
heaters = [2,30]

#houses = []
#heaters = [1]

print Solution().findRadius(houses, heaters)