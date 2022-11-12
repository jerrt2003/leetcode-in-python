# -*- coding: utf-8 -*-
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        Solution: Hashtable
        Time Complexity:O(n)
        Space Complexity:O(n)
        Thinking Process:
        :type J: str
        :type S: str
        :rtype: int
        """
        hashtable = {}
        for char in S:
            try:
                hashtable[char] += 1
            except:
                hashtable[char] = 1
        res = 0
        for char in J:
            try:
                res += hashtable[char]
            except:
                pass
        return res
