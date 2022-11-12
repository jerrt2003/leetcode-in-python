import math


class Solution(object):
    def minmaxGasDist(self, stations, K):
        """
        BS
        Runtime: 596 ms, faster than 62.64% of Python online submissions for Minimize Max Distance to Gas Station.
        Memory Usage: 13.1 MB, less than 28.09% of Python online submissions for Minimize Max Distance to Gas Station.
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        m = len(stations)
        def isValid(d):
            count = 0
            for i in range(m-1):
                count += math.ceil((stations[i+1]-stations[i])/d) - 1
            return count > K

        l, r = 1e-6, stations[-1]-stations[0]
        while r - l > 1e-6:
            mid = (l+r)/2
            if not isValid(mid):
                r = mid
            else:
                l = mid
        return l

print Solution().minmaxGasDist([1,2,3,4,5,6,7,8,9,10],9)