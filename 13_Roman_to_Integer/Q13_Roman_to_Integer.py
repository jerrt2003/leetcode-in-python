class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500, 'M':1000}
        if s is None or len(s) == 0:
            return 0
        res = 0
        i = 0
        while i < len(s)-1:
            if mapping[s[i]] < mapping[s[i+1]]:
                res -= mapping[s[i]]
            else:
                res += mapping[s[i]]
            i += 1
        return res + mapping[s[-1]]

sol = Solution()
print sol.romanToInt('IX')