class Solution(object):
    def maximizeSweetness(self, sweetness, K):
        """
        Greedy + BS
        T:O(nlog(n)) S:O(1)
        Runtime: 192 ms, faster than 72.24% of Python online submissions for Divide Chocolate.
        Memory Usage: 13.7 MB, less than 100.00% of Python online submissions for Divide Chocolate.
        :type sweetness: List[int]
        :type K: int
        :rtype: int
        """
        def notValidCut(i):
            cut = 0
            total = 0
            for s in sweetness:
                total += s
                if total >= i:
                    cut += 1
                    total = 0
            return cut < K+1

        l, r = min(sweetness), sum(sweetness)/(K+1)+1
        while l < r:
            m = (l+r-1)/2
            if notValidCut(m):
                r = m
            else:
                l = m+1
        return l-1

print Solution().maximizeSweetness([1,2,3,4,5,6,7,8,9], 5)