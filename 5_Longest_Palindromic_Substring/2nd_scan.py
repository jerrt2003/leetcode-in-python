# -*- coding: utf-8 -*-
class Solution(object):
    def longestPalindrome(self, s):
        """
        Solution: DP
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        Inspired By: https://leetcode.com/problems/longest-palindromic-substring/solution/
        Performance: T(7260 ms, beat 7.31%), M(104.9 MB, beat 18.83%)
        TP:
        - given a substring s' = s[i:j+1]
        - s' is palindromic if s[i] == s[j] && s[i+1:j-1] is also palindromic
        - thus this create a DP recursion relationship
        :type s: str
        :rtype: str
        """
        if not s: return s
        max_len = -float('inf')
        res = None
        m = n = len(s)
        DP = [[None for _ in range(n)] for _ in range(m)]

        def helper(i, j):
            if DP[i][j] is not None:
                return DP[i][j]
            elif j-i+1 == 2: # this is use to take care of even number situation (ex. 'abba' or 'cc')
                if s[i] == s[j]:
                    DP[i][j] = True
                else:
                    DP[i][j] = False
                return DP[i][j]
            elif i == j:
                DP[i][j] = True
                return DP[i][j]
            else:
                if helper(i + 1, j - 1) and s[i] == s[j]:
                    DP[i][j] = True
                else:
                    DP[i][j] = False
                return DP[i][j]

        for i in range(m):
            for j in range(i, n):
                if helper(i, j):
                    curr_len = j - i + 1
                    if curr_len > max_len:
                        max_len = curr_len
                        res = s[i:j + 1]
        return res


s = 'babad'
print Solution().longestPalindrome(s)