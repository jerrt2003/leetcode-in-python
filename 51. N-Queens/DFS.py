# -*- coding: utf-8 -*-
class Solution(object):
    def solveNQueens(self, n):
        """
        Solution: DFS
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/n-queens/discuss/19810/Fast-short-and-easy-to-understand-python-solution-11-lines-76ms
        TP:
        - Queens moement in chess: go vertical / go horizontal / go 45"(slope = 1) / go 135"(slope = -1)
        - Consider 2 node (x, y) and (p, q):
            - slope == 1:
                => (y-q)/(x-p) == 1 -> y-q = x-p -> x-y = p-q (DIFF)
             - slope == -1:
                => (y-q)/(x-p) == -1 -> y-q = -x+p -> x+y = p+q (SUM)
        :type n: int
        :rtype: List[List[str]]
        """
        res = []

        def DFS(queens_placement, xy_sum, xy_diff):
            '''
            :param queens_placement: To record 'Q' x-cord for each row
            :param xy_sum: To record x+y (sum) so far
            :param xy_diff: To record x-y (diff) so far
            :return:
            '''
            p = len(queens_placement)
            if p == n:
                res.append(queens_placement)
                return
            for q in range(n):
                if q not in queens_placement and p+q not in xy_sum and p-q not in xy_diff:
                    DFS(queens_placement+[q], xy_sum+[p+q], xy_diff+[p-q])
                    '''
                    queens_placement+[q] --> means we decide to put 'Q' at x-position: q at this row.
                    ex. [3, 1, 2] means we put 'Q' at x:3 for row 0, 'Q' at x:1 for row 1, 'Q' at x:2 for row 2
                        so next DFS we are dealing with Q's position at row 4
                    Condition:
                    1. Since we only put 1 'Q' at each row, so we can prevent duplicate Q in the same row (horizontal)
                    2. Since <q not in queens_placement>: we can prevent duplicate Q in the same col (vertical)
                    3. Since <p+q not in xy_sum and p-q not in xy_diff>: we can prevent duplicate Q at slope 1 or slope -1
                    '''

        DFS([],[],[])

        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in res]

n = 9
print Solution().solveNQueens(n)