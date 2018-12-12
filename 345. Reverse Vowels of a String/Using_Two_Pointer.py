# -*- coding: utf-8 -*-
class Solution(object):
    def reverseVowels(self, s):
        """
        Solution: Use 2-pointer from starting and end position
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: https://leetcode.com/problems/reverse-vowels-of-a-string/discuss/81233/Python-2-Pointers-Solution
        :type s: str
        :rtype: str
        """
        p1 = 0
        p2 = len(s)-1
        s = list(s)
        vowels = list('aeiuoAEIOU')
        while p1 < p2:
            if s[p1] in vowels and s[p2] in vowels: # swap
                s[p1],s[p2] = s[p2],s[p1]
                p1 += 1
                p2 -= 1
            elif s[p1] not in vowels:
                p1 += 1
            elif s[p2] not in vowels:
                p2 -= 1
        return ''.join(s)

s = 'leetcode'
print Solution().reverseVowels(s)