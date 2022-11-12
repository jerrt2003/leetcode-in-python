import collections


class Solution(object):
    def numberOfSubstrings(self, s):
        """
        T:O(n) S:O(1)
        Runtime: 384 ms, faster than 28.22% of Python online submissions for Number of Substrings Containing All Three Characters.
        Memory Usage: 14.8 MB, less than 100.00% of Python online submissions for Number of Substrings Containing All Three Characters.
        :type s: str
        :rtype: int
        """
        counter = {c:0 for c in 'abc'}
        l = len(s)
        res = 0
        j = 0
        for i in range(l):
            counter[s[i]] += 1
            while all(counter.values()):
                res += len(s)-i
                counter[s[j]] -= 1
                j += 1
        return res

print Solution().numberOfSubstrings("abcabc")