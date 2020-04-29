class Solution(object):
    def findMinFibonacciNumbers(self, k):
        """
        T:O(n+log(n)) S:O(n)
        Runtime: 28 ms, faster than 71.99% of Python online submissions for Find the Minimum Number of Fibonacci Numbers Whose Sum Is K.
        Memory Usage: 13.2 MB, less than 100.00% of Python online submissions for Find the Minimum Number of Fibonacci Numbers Whose Sum Is K.
        :type k: int
        :rtype: int
        """
        fibs = [1, 1]
        i = 1
        while i <= k:
            i = fibs[-1]+fibs[-2]
            fibs.append(i)

        if k in fibs:
            return 1

        def findMin(k, count):
            if k in fibs:
                return count+1
            return findMin(k-fibs[bs(k)-1], count+1)

        def bs(num):
            l, r = 0, len(fibs)
            while l < r:
                m = (l+r-1)/2
                if fibs[m] > num:
                    r = m
                else:
                    l = m+1
            return l

        return findMin(k-fibs[bs(k)-1], 1)

print Solution().findMinFibonacciNumbers(5)