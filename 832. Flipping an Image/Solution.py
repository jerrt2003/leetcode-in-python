# -*- coding: utf-8 -*-
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        Solution: O(m*n)
        Time Complexity: O(m*n)
        Space Complexity: O(1)
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        A = [row[::-1] for row in A]
        for row in A:
            for i in range(len(row)):
                row[i] = 0 if row[i] == 1 else 1
        return A

        # One Line Solution:
        # return [[1 ^ i for i in row[::-1]] for row in A]