import collections


class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return self.subArrayAtMostK(A,K) - self.subArrayAtMostK(A,K-1)


    def subArrayAtMostK(self, A, K):
        bkt = collections.defaultdict(int)
        i, j, ans = 0, 1, 1
        bkt[A[i]] += 1
        while j < len(A):
            bkt[A[j]] += 1
            while len(bkt) > K:
                bkt[A[i]] -= 1
                if bkt[A[i]] == 0:
                    del bkt[A[i]]
                i += 1
            ans += j-i+1
            j += 1
        return ans

# print Solution().subarraysWithKDistinct([1,2,1,3,4], 3)
print Solution().subarraysWithKDistinct([1,2], 1)