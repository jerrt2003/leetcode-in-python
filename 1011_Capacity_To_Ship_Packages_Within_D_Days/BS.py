# -*- coding: utf-8 -*-
class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        def isValid(target):
            total = 0
            day = 1
            for w in weights:
                total += w
                if total > target:
                    day += 1
                    total = w
                    if day > D:
                        return False
            return True

        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l+r)/2
            if isValid(mid):
                r = mid
            else:
                l = mid+1
        return l

weights = [1,2,3,1,1]
D = 4

print Solution().shipWithinDays(weights, D)