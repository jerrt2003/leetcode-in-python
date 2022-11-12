class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        find the smallest sub-array sum which length is len(cardPoints)-k
        sliding window
        T:O(n) S:O(1)
        Runtime: 428 ms, faster than 65.93% of Python online submissions for Maximum Points You Can Obtain from Cards.
        Memory Usage: 23.2 MB, less than 100.00% of Python online submissions for Maximum Points You Can Obtain from Cards.
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        pt1 = pt2 = 0
        min_subarray_sum = float('inf')
        subarray_sum = 0
        m = len(cardPoints)-k
        while pt2 < len(cardPoints):
            while pt2-pt1+1 > m:
                subarray_sum -= cardPoints[pt1]
                pt1 += 1
            subarray_sum += cardPoints[pt2]
            if pt2-pt1+1 == m:
                min_subarray_sum = min(min_subarray_sum, subarray_sum)
            pt2 += 1
        return sum(cardPoints) - min_subarray_sum

print Solution().maxScore([1,2,3,4,5,6,1], 3)
print Solution().maxScore([2,2,2], 2)
print Solution().maxScore([9,7,7,9,7,7,9], 7)
print Solution().maxScore([1,1000,1], 1)
print Solution().maxScore([], 3)
