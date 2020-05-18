import collections


class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        DP + Sliding Window (Monotonic Queue)
        T:O(n) S:O(k)
        DP equation: DP[i] = max(DP[i-1],DP[i-2]...DP[i-k],0) + nums[i]
        Runtime: 520 ms, faster than 69.28% of Python online submissions for Constrained Subsequence Sum.
        Memory Usage: 32.5 MB, less than 100.00% of Python online submissions for Constrained Subsequence Sum.
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        DP = collections.defaultdict(int)
        queue = []
        ret = -float('inf')
        for i in range(len(nums)):
            if i > k and queue[0] == i-k-1:
                queue.pop(0)
            if not queue:
                DP[i] = nums[i]
            else:
                DP[i] = max(DP[queue[0]],0) + nums[i]
            while queue and DP[i] > DP[queue[-1]]:
                queue.pop()
            queue.append(i)
            ret = max(ret, DP[i])
        return ret

print Solution().constrainedSubsetSum([10,2,-10,5,20],2)