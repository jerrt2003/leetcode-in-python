# -*- coding: utf-8 -*-
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
        if not A or not B:
            return None

        for i, row in enumerate(A):
            for j, col in enumerate(zip(*B)):
                for k, (a, b) in enumerate(zip(row, col)):
                    res[i][k] += a*b

        return res

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

assert Solution().multiply(A, B) == [[7,0,0],[-7,0,3]]