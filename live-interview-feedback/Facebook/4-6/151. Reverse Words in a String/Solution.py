# -*- coding: utf-8 -*-
class Solution(object):
    def reverseWords(self, s):
        """
        Solution: using split in python
        Time Complexity: O(n)
        Space Complexity: O(n)
        TP:
        - python split() w/o any given spacer will split "any" number of white spaces
        :type s: str
        :rtype: str
        """
        input = s.strip(' ').split()
        res = ''
        for word in input[::-1]:
            res = res + word + ' '
        return res.strip(' ')

s = "the sky is blue"
sol = Solution()
print sol.reverseWords(s)