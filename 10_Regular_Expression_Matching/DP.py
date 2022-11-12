# -*- coding: utf-8 -*-
class Solution(object):
    def isMatch(self, s, p):
        """
        Solution: DP
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        Inspired By: https://www.youtube.com/watch?v=l3hda49XcDE
        Algorithm:
            - s: string, p: pattern
            - create 2-D boolean array DP: len(s)+1 * len(p)+1
            - DP[0][0] is True: because empty s will have a match for empty p
            - For every DP[0][j] = False: because empty s will never have a match for any non-empty p
            - For every DP[i][0] = False: because empty p will never have a match for any non-empty s
            - Go through the s and try to match each p:
                - if s[i] == p[j] or p[j] == '.': DP[i][j] == DP[i-1][j-1] => we can discard the last character
                (since already a match) and just find if previous s, p is match or not (DP[i-1][j-1]
                - if p[j] == '*', we will have following three condition:
                    - DP[i][j] = DP[i][j-2] => 0 occurrence(attention: * mean 0 or more previous character so s: empty,
                    p: a* is a match since a* can be empty string)
                    - if p[j-1] == s[i] or p[j-1] == '.': DP[i][j] = DP[i-1][j] (a* repeat once or more than once)
            - return DP[len(s)+1][len(p)+1]
        :type s: str
        :type p: str
        :rtype: bool
        """
        len_s = len(s)
        len_p = len(p)
        DP = [[False for _ in range(len_p+1)] for _ in range(len_s+1)]
        DP[0][0] = True

        # special case: s is empty and p is 'a*' or 'a*b*'...
        for j in range(1, len_p+1):
            if p[j-1] is '*':
                DP[0][j] = DP[0][j-2]

        for i in range(1, len_s+1):
            for j in range(1, len_p+1):
                if s[i-1] == p[j-1] or p[j-1] is '.':
                    DP[i][j] = DP[i-1][j-1]
                elif p[j-1] is '*':
                    DP[i][j] = DP[i][j-2]
                    if s[i-1] is p[j-2] or p[j-2] is '.':
                        DP[i][j] = DP[i][j] or DP[i-1][j]
        return DP[-1][-1]


s = "aa"
p = "a*"

sol = Solution()
print sol.isMatch(s,p)
