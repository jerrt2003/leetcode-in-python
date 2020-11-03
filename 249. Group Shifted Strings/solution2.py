import collections


class Solution(object):
    def groupStrings(self, strings):
        """
        Facebook
        T:O(n) S:O(n)
        Runtime: 20 ms, faster than 95.43% of Python online submissions for Group Shifted Strings.
        Memory Usage: 12.8 MB, less than 64.47% of Python online submissions for Group Shifted Strings.
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        ans = collections.defaultdict(list)
        for s in strings:
            key = []
            for i in range(len(s)-1):
                diff = 26 + ord(s[i+1]) - ord(s[i])
                key.append(diff % 26)
            ans[tuple(key)].append(s)

        return ans.values()

print Solution().groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"])