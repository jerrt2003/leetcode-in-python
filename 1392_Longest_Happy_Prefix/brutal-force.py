class Solution(object):
    def longestPrefix(self, s):
        """
        brutal force
        Runtime: 8216 ms, faster than 13.34% of Python online submissions for Longest Happy Prefix.
        Memory Usage: 18 MB, less than 100.00% of Python online submissions for Longest Happy Prefix.
        :type s: str
        :rtype: str
        """
        for i in range(len(s)-1, 0, -1):
            if s[:i] == s[-i:]:
                return s[:i]
        return ""

print Solution().longestPrefix("ababab")