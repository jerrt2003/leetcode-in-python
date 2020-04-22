# -*- coding: utf-8 -*-
class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        ages.sort()
        count = 0
        def request(age, arr, count):
            l, r = 0, len(arr)
            while l < r:
                mid = (l+r-1)/2
                if arr[mid] > 0.5 * age + 7:
                    r = mid
                else:
                    l = mid+1
            return (len(arr)-l)

        for i, a in enumerate(ages):
            count += request(a, ages[:i], count)

assert Solution().numFriendRequests([16,16]) == 2
assert Solution().numFriendRequests([16,17,18]) == 2