class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        nxt = self.kmpBuild(s)
        if nxt[-1] == 0:
            return False
        return len(s) % (len(s)-nxt[-1]) == 0


    def kmpBuild(self, s):
        nxt = [0, 0]
        j = 0
        l = len(s)
        for i in range(1, l):
            while j > 0 and s[i] != s[j]:
                j = nxt[j]
            if s[i] == s[j]:
                j += 1
            nxt.append(j)
        return nxt

print Solution().repeatedSubstringPattern("abdfab")