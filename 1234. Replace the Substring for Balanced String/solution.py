import collections


class Solution(object):
    def balancedString(self, s):
        """
        sliding window
        T:O(n) S:O(n)
        Runtime: 652 ms, faster than 33.57% of Python online submissions for Replace the Substring for Balanced String.
        Memory Usage: 16.6 MB, less than 22.86% of Python online submissions for Replace the Substring for Balanced String.
        :type s: str
        :rtype: int
        """
        counter = collections.Counter(s)
        l, ans, j = len(s), float('inf'), 0
        for i in range(l):
            counter[s[i]] -= 1
            while j < l and all(l/4 >= counter[c] for c in 'QWER'):
                ans = min(ans, i-j+1)
                counter[s[j]] += 1
                j += 1
        return ans


print Solution().balancedString('QWER')