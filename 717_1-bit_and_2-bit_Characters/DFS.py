# -*- coding: utf-8 -*-
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        def DFS(bits):
            if len(bits) == 1 and bits[0] == 0:
                return True
            elif not bits:
                return False
            elif bits[0] == 0:
                if DFS(bits[1:]):
                    return True
            elif bits[0:2] == [1, 0] or bits[0:2] == [1, 1]:
                if DFS(bits[2:]):
                    return True
            return False

        return DFS(bits)

bits = [1, 1, 1, 0]
print Solution().isOneBitCharacter(bits)