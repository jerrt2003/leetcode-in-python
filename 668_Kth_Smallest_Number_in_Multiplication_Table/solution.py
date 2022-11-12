class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        Binary Search
        T:O(mnlog(m*n)) S: O(1)
        Runtime: 636 ms, faster than 70.00% of Python online submissions for Kth Smallest Number in Multiplication Table.
        Memory Usage: 13.3 MB, less than 42.86% of Python online submissions for Kth Smallest Number in Multiplication Table.
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def enough(x):
            # T:O(mn) S:O(1)
            count = 0
            for i in range(1, m+1):
                count += min(x/i, n)
            return count >= k

        l, r = 1, m*n+1
        while l < r:
            # T: O(log(n)) S:O(1)
            mid = (l+r-1)/2
            if enough(mid):
                r = mid
            else:
                l = mid+1
        return l


print Solution().findKthNumber(3,3,5)
print Solution().findKthNumber(2,3,6)