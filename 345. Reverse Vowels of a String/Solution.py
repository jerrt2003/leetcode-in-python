# -*- coding: utf-8 -*-
class Solution(object):
    def reverseVowels(self, s):
        """
        Solution: (TLE)
        Time Complexity: O(2n)
        Space Complexity: O(n)
        TP:
        - TLE
        :type s: str
        :rtype: str
        """
        tmp_res = []
        tmp_vowels = []
        vowels = ['A','a','E','e','I','i','O','o','U','u']
        for char in s:
            if char in vowels:
                tmp_vowels.append(char)
                tmp_res.append('*')
            else:
                tmp_res.append(char)
        res = ''
        for char in tmp_res:
            if char == '*':
                res += tmp_vowels.pop()
            else:
                res += char
        return res

s = 'leetcode'
print Solution().reverseVowels(s)