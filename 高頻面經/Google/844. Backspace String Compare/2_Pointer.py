# -*- coding: utf-8 -*-
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        T: O(n)
        S: O(1)
        Perf: Runtime: 16 ms, faster than 91.36% / Memory Usage: 11.7 MB, less than 53.10%
        :type S: str
        :type T: str
        :rtype: bool
        """

        def finalString(string):
            res = ''
            skip = 0
            for c in string[::-1]:
                if c == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    res += c
            return res

        return finalString(S) == finalString(T)
