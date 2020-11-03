class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        BS
        T:O(nlog(n)) S:O(1)
        Runtime: 460 ms, faster than 48.99% of Python online submissions for Koko Eating Bananas.
        Memory Usage: 13.7 MB, less than 48.55% of Python online submissions for Koko Eating Bananas.
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        def bs(K):
            count = 0
            for pile in piles:
                count += pile/K
                if pile%K != 0:
                    count += 1
                if count > H:
                    return False
            return count <= H

        l, r = 1, max(piles)+1
        while l < r:
            m = (l+r-1)/2
            if bs(m):
                r = m
            else:
                l = m+1
        return l

print Solution().minEatingSpeed([3,6,7,11], 8)
print Solution().minEatingSpeed([30,11,23,4,20], 5)
print Solution().minEatingSpeed([30,11,23,4,20], 6)