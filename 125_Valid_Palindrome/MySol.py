# -*- coding: utf-8 -*-
import re
class Solution(object):
    def isPalindrome(self, s):
        """
        Solution: Use 2-pointer
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: MYSELF!!
        :type s: str
        :rtype: bool
        """
        p = re.compile('[a-z0-9]')
        filter_s = ''.join([char for char in s.lower() if p.match(char)])
        '''
        left = 0
        right = len(filter_s)-1
        while left <= right:
            if filter_s[left] == filter_s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
        '''
        if filter_s == filter_s[::-1]:
            return True
        return False

#s = "A man, a plan, a canal: Panama"
#s = "race a car"
s = '0P'
print Solution().isPalindrome(s)
