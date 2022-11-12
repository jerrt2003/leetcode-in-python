# -*- coding: utf-8 -*-
class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        count = 0
        for i, v in enumerate(ages):
            for j, w in enumerate(ages):
                if i == j:
                    continue
                if w <= v*0.5 + 7 or w > v or (w > 100 and v < 100):
                    continue
                else:
                    count += 1
        return count

assert Solution().numFriendRequests([16,16]) == 2