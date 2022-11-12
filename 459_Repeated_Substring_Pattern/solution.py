class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = len(s)
        for i in range(m/2):
            x = len(s[:i + 1])
            if m % x != 0:
                continue
            p = m/x
            if s[:i+1]*p == s:
                return True
        return False

print Solution().repeatedSubstringPattern("abcabc")