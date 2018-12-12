# -*- coding: utf-8 -*-
from Queue import PriorityQueue as queue
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        Solution: Heap(Priority Queue)
        Time Complexity:
        Space Complexity: O(n)
        Inspired By: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85173/Share-my-thoughts-and-Clean-Java-Code
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if matrix is None or len(matrix) == 0: return None
        q = queue()
        for i in range(len(matrix[0])):
            q.put((matrix[0][i], (0, i)))
        for i in range(k-1):
            _node = q.get()
            location = _node[1]
            if location[0] == len(matrix)-1:
                continue
            q.put((matrix[location[0]+1][location[1]], (location[0]+1,location[1])))
        res = q.get()
        return res[0]
'''
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
'''
matrix = []
k = 1

print Solution().kthSmallest(matrix, k)

