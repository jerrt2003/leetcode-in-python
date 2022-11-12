# -*- coding: utf-8 -*-
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        Solution: List(Hashtable)
        Time Complexity:O(n)
        Space Complexity:O(n)
        Thinking Process:
        - This is still a hashtable solution since we use 'in' function call
        :type J: str
        :type S: str
        :rtype: int
        """
        res = 0
        for s in S:
            if s in J:
                res+=1
        return res