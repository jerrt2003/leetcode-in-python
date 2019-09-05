# -*- coding: utf-8 -*-
class Solution(object):
    def cutToDetermineIfPalindrome(self, s1, s2):

        def isPalindrome(input):
            l, r = 0, len(input)
            while l < r:
                if input[l] != input[r]:
                    return False
                l += 1
                r -= 1
            return True

        i, res = 0, []
        while i < len(s1) and i < len(s2):
            if isPalindrome(s1[:i]+s2[i:]) or isPalindrome(s2[:i]+s1[i:]):
                res.append(i)
            i += 1

