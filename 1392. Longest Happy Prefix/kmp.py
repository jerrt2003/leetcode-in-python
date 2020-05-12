class Solution(object):
    def longestPrefix(self, s):
        """
        KMP
        T:O(n) S:O(n)
        Runtime: 292 ms, faster than 74.02% of Python online submissions for Longest Happy Prefix.
        Memory Usage: 20.9 MB, less than 100.00% of Python online submissions for Longest Happy Prefix.
        :type s: str
        :rtype: str
        """
        m = len(s)
        nxt = [0, 0]
        j = 0
        for i in range(1, m):
            while j > 0 and s[i] != s[j]:
                j = nxt[j]
            if s[i] == s[j]:
                j += 1
            nxt.append(j)
        return s[0:nxt[-1]]

print Solution().longestPrefix("a")