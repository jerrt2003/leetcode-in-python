class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        for group in zip(*strs):
            if len(set(group)) == 1:
                result += group[0]
            else:
                return result
        return result

a = ["",""]
sol = Solution()
print sol.longestCommonPrefix(a)
