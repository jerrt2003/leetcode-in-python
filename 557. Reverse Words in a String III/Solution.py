# -*- coding: utf-8 -*-
class Solution(object):
    def reverseWords(self, s):
        """
        Solution
        Time Complexity:
        Space Complexity:
        Inspired By: MYSELF!!
        :type s: str
        :rtype: str
        """
        return " ".join([i[::-1] for i in s.split()])
        '''
        res = ''
        for word in s.split():
            res += word[::-1] + ' '
        return res.strip()
        '''

#s = "Let's take LeetCode contest"
s = ''
print Solution().reverseWords(s)