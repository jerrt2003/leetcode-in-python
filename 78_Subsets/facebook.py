class Solution(object):
    def subsets(self, nums):
        """
        Facebook
        T:O(n*n^2) S:O(n*n^2)
        Runtime: 20 ms, faster than 85.17% of Python online submissions for Subsets.
        Memory Usage: 12.9 MB, less than 28.79% of Python online submissions for Subsets.
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]

        def dfs(lst, subset):
            if not lst:
                return
            for i in range(len(lst)):
                ans.append(subset + [lst[i]])
                dfs(lst[i + 1:], subset + [lst[i]])

        dfs(nums,[])
        return ans
print Solution().subsets([1,2,3])