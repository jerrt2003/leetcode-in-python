class Solution(object):
    def numDecodings(self, s):
        """
        Facebook
        T:O(n) S:O(1)
        Runtime: 28 ms, faster than 51.01% of Python online submissions for Decode Ways.
        Memory Usage: 14.1 MB, less than 12.06% of Python online submissions for Decode Ways.
        :type s: str
        :rtype: int
        """
        DP = dict()

        def dfs(i):
            if i >= len(s):
                return 1
            if i in DP:
                return DP[i]
            total = 0
            for j in [i + 1, i + 2]:
                if j > len(s):
                    break
                if s[i] == '0':
                    break
                if 1 <= int(s[i:j]) <= 26:
                    total += dfs(j)
            DP[i] = total
            return DP[i]

        return dfs(0)


print Solution().numDecodings("1024")