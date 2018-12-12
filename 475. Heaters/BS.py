# -*- coding: utf-8 -*-
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        Solution: BS
        Time Complexity: max(O(nlog(n)), m(log(m)))
        Space Complexity: O(1)
        Inspired By: https://leetcode.com/problems/heaters/discuss/95886/Short-and-Clean-Java-Binary-Search-Solution
        TP:
        - Using the BS to decide each house's location in 'heaters' list
        - Then we choose the min distance between house and its left heater and right heater (house_to_heater_distance)
            - As long as a house is covered by one heater, then condition will suffice, thus we choose min
        - Then we choose the max(house_to_heater_distance) to get min heater radius
        - 2 corner cases:
            - if house at left most of heater's list, then there are no left heater_to_house_distance
            - if house at right most of heater's list, then there are no right heater_to_house_distance
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        if len(houses) == 0 or len(heaters) == 0: return 0
        def findPosition(target):
            l = 0
            r = len(heaters)
            while l < r:
                m = (l+r)/2
                if target > heaters[m]:
                    l = m+1
                else:
                    r = m
            return l

        houses.sort()
        heaters.sort()
        res = -float('inf')
        for house in houses:
            _pos = findPosition(house)
            if _pos == 0:
                res = max(res, heaters[0]-house)
            elif _pos == len(heaters):
                res = max(res, house - heaters[-1])
            else:
                res = max(res, min(house-heaters[_pos-1], heaters[_pos]-house)) # !!! tricky: _pos 實際上算是找出house在heaters的相對位置
        return res

#houses = [1,2,3]
#heaters = [2]

#houses = [1,2,3,4]
#heaters = [1,4]

#houses = [1,2,3,5,15]
#heaters = [2,30]

houses = []
heaters = [1]

print Solution().findRadius(houses, heaters)