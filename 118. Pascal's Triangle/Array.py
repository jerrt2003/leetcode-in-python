# -*- coding: utf-8 -*-
class Solution(object):
    def generate(self, numRows):
        """
        Solution: Array
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MYSELF!!
        TP:
        - a bit of DP
        - initial res with [1] and [1,1] (if numRows > 2)
        - then just follow the pascal triangle logic
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            if i == 0:
                res.append([1])
            elif i == 1:
                res.append([1,1])
            else:
                res.append(self._create_middle_number(res[-1]))
        return res

    def _create_middle_number(self, previous_row):
        new_row = [1]
        for idx in range(len(previous_row)-1):
            new_row.append(previous_row[idx]+previous_row[idx+1])
        new_row.append(1)
        return new_row


num = 5
sol = Solution()
print sol.generate(5)
