class Solution(object):
    def findStrobogrammatic(self, n):
        """
        Facebook
        T:O(5^n) S:O(n)
        Runtime: 112 ms, faster than 51.38% of Python online submissions for Strobogrammatic Number II.
        Memory Usage: 20 MB, less than 9.18% of Python online submissions for Strobogrammatic Number II.
        :type n: int
        :rtype: List[str]
        """
        mirror = {"0":"0","1":"1","6":"9","8":"8","9":"6"}
        ans = []

        def dfs(nums, l, r):
            if l > r:
                ans.append(''.join(nums))
                return
            for k, v in mirror.iteritems():
                if l == r and k in ("6","9"): continue
                if l != r and l == 0 and k == "0": continue
                nums[l], nums[r] = k, v
                dfs(nums, l+1, r-1)

        dfs([None] * n, 0, n-1)

        return ans

print Solution().findStrobogrammatic(4)