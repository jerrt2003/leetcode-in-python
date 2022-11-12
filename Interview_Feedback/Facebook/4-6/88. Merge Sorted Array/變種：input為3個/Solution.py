# -*- coding: utf-8 -*-
import pq
class Solution(object):
    def sortNArray(self, nums1, nums2, nums3):
        """
        Time Complexity: O(nlog(k))
        Space Complexity: O(k)
        :param nums1:
        :param nums2:
        :param nums3:
        :return:
        """
        pq = []
        res = []
        if nums1:
            pq.heappush(pq, (nums1.pop(0), 1))
        if nums2:
            pq.heappush(pq, (nums2.pop(0), 2))
        if nums3:
            pq.heappush(pq, (nums3.pop(0), 3))
        while pq:
            num, arrayIdx = pq.heappop(pq)
            if num not in res:
                res.append(num)
            if arrayIdx == 1:
                if nums1:
                    pq.heappush(pq, (nums1.pop(0), 1))
            elif arrayIdx == 2:
                if nums2:
                    pq.heappush(pq, (nums2.pop(0), 2))
            else:
                if nums3:
                    pq.heappush(pq, (nums3.pop(0), 3))
        return res

assert Solution().sortNArray([1,2,3,10],[2,2,4,7],[3,3,9,11,12]) == [1,2,3,4,7,9,10,11,12]

