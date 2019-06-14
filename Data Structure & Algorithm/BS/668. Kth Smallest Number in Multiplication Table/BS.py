# -*- coding: utf-8 -*-
class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        Solution: BS
        Time Complexity: m*log(m*n)
        Space Complexity: O(1)
        Perf: Runtime: 656 ms, faster than 46.03% / Memory Usage: 12.5 MB, less than 25.00%
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """

        def check(x):
            count = 0
            for i in range(1, m + 1):
                count += min(n, x / i)
            return count >= k

        l, r = 1, m * n + 1
        while l < r:
            mid = (l + r - 1) / 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l


assert Solution().findKthNumber(2,3,6)