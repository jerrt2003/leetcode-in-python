class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m, n = len(haystack), len(needle)
        if n == 0:
            return 0
        nxt = self.build(needle)
        j = 0
        for i in range(m):
            while j > 0 and haystack[i] != needle[j]:
                j = nxt[j]
            if haystack[i] == needle[j]:
                j += 1
            if j == n:
                return i-j+1
        return -1


    def build(self, needle):
        m = len(needle)
        nxt = [0, 0]
        j = 0
        for i in range(1, m):
            while j > 0 and needle[i] != needle[j]:
                j = nxt[j]
            if needle[i] == needle[j]:
                j += 1
            nxt.append(j)
        return nxt

print Solution().strStr("a","")