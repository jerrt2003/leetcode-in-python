# -*- coding: utf-8 -*-
class Solution(object):
    def findMinResource(self, tasks, k):

        def countResource(m):
            count = 1
            curr = 0
            for task in tasks:
                if curr + task > m:
                    count += 1
                    curr = task
                else:
                    curr += task
            return count <= k

        l, r = max(tasks), sum(tasks)
        while l < r:
            mid = (l+r-1)/2
            if countResource(mid):
                r = mid
            else:
                l = mid+1
        return l

#assert Solution().findMinResource([2,3,5,2,6,5], 3) == 10
assert Solution().findMinResource([2,3,5,2,6,5], 5) == 6