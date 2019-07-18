# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
class Solution(object):

    def __init__(self, arr):
        self.tree = FenwickTree(arr)

    def update(self, i, j):
        self.tree.update(i+1, 1)
        self.tree.update(j+2, -1)

    def query(self, i):
        res = self.tree.query(i+1)
        return res % 2 == 1


class FenwickTree(object):

    def __init__(self, arr):
        self.tree = [0 for _ in range(len(arr)+1)]

    def update(self, i, diff):
        while i < len(self.tree):
            self.tree[i] += diff
            i += (i & -i)

    def query(self, i):
        sum = 0
        while i > 0:
            sum += self.tree[i]
            i -= (i & -i)
        return sum

N = 5
light = Solution([0,0,0,0,0])

light.update(0, 1)
light.update(1, 2)
print light.query(1)
