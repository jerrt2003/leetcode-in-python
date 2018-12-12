# -*- coding: utf-8 -*-
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        Solution: Hashmap (dict)
        Time Complexity: O(2*n^2) = O(n^2)
        Space Complexity: O(n^2)
        Inspired By: https://leetcode.com/problems/4sum-ii/discuss/93946/Simple-Java-Solution-with-Explanation
        TP:
        - Take the arrays A and B, and compute all the possible sums of two elements.
          Put the sum in the Hash map, and increase the hash map value if more than 1 pair sums to the same value.
        - Compute all the possible sums of the arrays C and D.
          If the hash map contains the opposite value of the current sum, increase the count of four elements sum to 0
          by the counter in the map.
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB_SUM = dict()
        for a in A:
            for b in B:
                sum = a + b
                if sum in AB_SUM:
                    AB_SUM[sum] += 1
                else:
                    AB_SUM[sum] = 1
        count = 0
        for c in C:
            for d in D:
                sum = c + d
                if -sum in AB_SUM:
                    count += AB_SUM[-sum]
        return count

#A = [ 1, 2]
#B = [-2,-1]
#C = [-1, 2]
#D = [ 0, 2]

A = []
B = []
C = []
D = []

print Solution().fourSumCount(A, B, C, D)