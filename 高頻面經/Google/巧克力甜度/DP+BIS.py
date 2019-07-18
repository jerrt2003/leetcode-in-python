# -*- coding: utf-8 -*-
class Solution(object):
    def splitChocolate(self, nums, k):
        """
        Problem Size: [ 1, len(nums) )
        Split: [1, k+1)
        start idx: [ 0, len(nums) )
        :param nums:
        :return:
        """
        m = len(nums)
        tree = FenwickTree(m)
        for i, v in enumerate(nums, 1):
            tree.update(i, v)

        DP = [[0]*(k+1) for _ in range(m+1)]
        DP[0][0] = float('inf')

        for i in range(1, m+1):
            for j in range(1, k+1):
                for c in range(i):
                    tmp = tree.query(i) - tree.query(c)
                    DP[i][j] = max(DP[i][j], min(DP[c][j-1], tmp))

        return DP[-1][-1]



class FenwickTree(object):
    def __init__(self, N):
        self.tree = [0]*(N+1)

    def update(self, idx, delta):
        while idx < len(self.tree):
            self.tree[idx] += delta
            idx += idx & (-idx)

    def query(self, idx):
        ret = 0
        while idx > 0:
            ret += self.tree[idx]
            idx -= idx & (-idx)
        return ret


nums = [3,2,3,1,4]
k = 3
assert Solution().splitChocolate(nums, k) == 4