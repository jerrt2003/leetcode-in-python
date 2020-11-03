class Solution(object):
    def longestOnes(self, A, K):
        """
        Facebook
        T:O(n) S:O(1)
        Runtime: 596 ms, faster than 51.81% of Python online submissions for Max Consecutive Ones III.
        Memory Usage: 13.6 MB, less than 12.50% of Python online submissions for Max Consecutive Ones III.
        sliding window -> longest substring with at most K 0s
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        l, j, ans = len(A), 0, -float('inf')
        for i in range(l):
            if A[i] == 0:
                K -= 1
            while K < 0:
                if A[j] == 0:
                    K += 1
                j += 1
            ans = max(ans, i-j+1)
        return ans

print Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)
print Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)