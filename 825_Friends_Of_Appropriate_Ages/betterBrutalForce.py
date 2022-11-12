# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def numFriendRequests(self, ages):
        """
        Perf: Runtime: 352 ms, faster than 42.62% / Memory Usage: 12.3 MB, less than 50.00%
        T: O(n*2)
        S: O(n)
        :type ages: List[int]
        :rtype: int
        """
        def request(a, b):
            return not ((b <= a*0.5+7) or (b > a) or (b>100 and a<100))

        counter = collections.Counter(ages)
        count = 0
        for a in counter.keys():
            for b in counter.keys():
                if a == b and request(a, b):
                    count += counter[a] * (counter[b] - 1)
                elif a != b and request(a, b):
                    count += counter[a] * counter[b]

        return count






#assert Solution().numFriendRequests([16,16]) == 2
assert Solution().numFriendRequests([16,17,18]) == 2
