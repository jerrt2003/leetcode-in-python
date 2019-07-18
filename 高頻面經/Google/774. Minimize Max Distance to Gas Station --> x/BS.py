# -*- coding: utf-8 -*-
class Solution(object):
    def minmaxGasDist(self, stations, K):
        def possible(D):
            return sum(int((stations[i+1] - stations[i]) / D)
                       for i in xrange(len(stations) - 1)) <= K

        lo, hi = 0, 10**8
        while hi - lo > 1e-6:
            mi = (lo + hi) / 2.0
            if possible(mi):
                hi = mi
            else:
                lo = mi
        return lo

stations = [1,2,3,4,5,6,7,8,9,10]
K = 9
assert Solution().minmaxGasDist(stations, K) == 0.5