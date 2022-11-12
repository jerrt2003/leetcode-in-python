class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        code_set = set()
        l = len(s)
        for i in range(l-k+1):
            code_set.add(s[i:i+k])
        return True if len(code_set) == 2**k else False

print Solution().hasAllCodes('0000000001011100',4)