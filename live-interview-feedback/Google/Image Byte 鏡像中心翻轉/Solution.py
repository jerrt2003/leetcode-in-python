# -*- coding: utf-8 -*-
class Solution(object):
    def imageMirror(self, bytes):
        """
        T: O(m*n*4)
        S: O(1)
        :param byte: List[List]
        :return: List[List]
        """
        for byte in bytes:
            byte[0], byte[1] = byte[1], byte[0]
            for _byte in byte:
                i, j = 0, len(_byte)
                while i < j:
                    _byte[i], _byte[j] = _byte[j], _byte[i]