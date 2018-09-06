class Solution(object):
    def lengthOfLIS(self, nums):
        """
        Method: DP
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        Solution From: https://leetcode.com/problems/longest-increasing-subsequence/discuss/74836/My-easy-to-understand-O(n2)-solution-using-DP-with-video-explanation
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        DP = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    DP[i] = max(DP[j]+1, DP[i])
        return max(*DP)




a = [10,9,2,5,3,7,101,18]
sol = Solution()
print sol.lengthOfLIS(a)