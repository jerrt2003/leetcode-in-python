class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        Sliding Window
        T:O(n) S:O(1)
        Runtime: 256 ms, faster than 48.04% of Python online submissions for Binary Subarrays With Sum.
        Memory Usage: 14 MB, less than 100.00% of Python online submissions for Binary Subarrays With Sum.
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        if S == 0:
            return self.atMost(A, S)
        return self.atMost(A, S) - self.atMost(A, S-1)


    def atMost(self, A, S):
        l, j, ans = len(A), 0, 0
        for i in range(l):
            if A[i] == 1:
                S -= 1
            while S < 0:
                if A[j] == 1:
                    S += 1
                j += 1
            ans += i-j+1
        return ans

print Solution().numSubarraysWithSum([[0,0,0,0,0], 0])