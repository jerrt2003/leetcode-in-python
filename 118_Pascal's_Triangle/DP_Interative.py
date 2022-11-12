# -*- coding: utf-8 -*-
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return []
        res = [[1]]
        for level in range(1, numRows):
            pre_row = res[-1]
            tmp_res = []
            for i in range(len(pre_row)):
                if i == 0:
                    tmp_res.append(1)
                else:
                    tmp_res.append(pre_row[i-1]+pre_row[i])
            tmp_res.append(1)
            res.append(tmp_res)
        return res