class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle is None or len(needle) == 0:
            return 0
        for i in range(0, len(haystack)):
            if len(haystack) - i < len(needle):
                return -1
            tmp = i
            found = 0
            for j in range(0, len(needle)):
                if needle[j] is haystack[tmp]:
                    tmp += 1
                    found += 1
                if found == len(needle):
                    return i
        return -1

haystack = ""
needle = ""
sol = Solution()
print sol.strStr(haystack,needle)