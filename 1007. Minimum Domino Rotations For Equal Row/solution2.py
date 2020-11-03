import collections
from collections import Counter


class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        counter_A = Counter(A)
        counter_B = Counter(B)
        same = collections.defaultdict(int)
        for i, j in zip(A, B):
            if i == j:
                same[i] += 1

        for i in range(1, 7):
            if counter_A[i]+counter_B[i]-same[i] == len(A):
                return min(counter_A[i], counter_B[i]) - same[i]
        return -1