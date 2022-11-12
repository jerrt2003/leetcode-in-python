import collections


class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        T:O(n) S:O(n)
        Runtime: 760 ms, faster than 19.39% of Python online submissions for Subarrays with K Different Integers.
        Memory Usage: 15 MB, less than 100.00% of Python online submissions for Subarrays with K Different Integers.
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return self.subArrayAtMostK(A,K) - self.subArrayAtMostK(A,K-1)

    def subArrayAtMostK(self, A, K):
        counter = collections.Counter()
        pt1 = pt2 = 0
        l = len(A)
        res = 0
        while pt2 < l:
            counter[A[pt2]] += 1
            while len(counter) > K:
                counter[A[pt1]] -= 1
                if counter[A[pt1]] == 0:
                    del counter[A[pt1]]
                pt1 += 1
            # https://youtu.be/FZPtxuxArLU?t=1146
            res += pt2-pt1+1
            pt2 += 1
        return res

print Solution().subarraysWithKDistinct([1,2,1,3,4], 3)
# print Solution().subarraysWithKDistinct([1,2], 1)