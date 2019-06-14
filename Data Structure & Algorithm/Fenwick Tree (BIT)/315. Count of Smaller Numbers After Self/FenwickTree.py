# -*- coding: utf-8 -*-
class Solution(object):
    def countSmaller(self, nums):
        """
        Solution: Fenwick Tree(BIT)
        Time Complexity: O(nlog(n))
        Space Complexity: O(n)
        :type nums: List[int]
        :rtype: List[int]
        """
        _sort_nums = sorted(set(nums))
        maps = {}
        for i, v in enumerate(_sort_nums, 1):
            maps[v] = i
        nums = nums[::-1]
        ranks = []
        for num in nums:
            ranks.append(maps[num])
        fenwickTree = FenwickTree(len(_sort_nums))
        res = []
        for rank in ranks:
            res.append(fenwickTree.query(rank-1))
            fenwickTree.update(rank, 1)
        return res[::-1]

class FenwickTree(object):
    def __init__(self, n):
        self.tree = [0]*(n+1)

    def update(self, i, delta):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i&(-i)

    def query(self, i):
        _sum = 0
        while i > 0:
            _sum += self.tree[i]
            i -= i&(-i)
        return _sum


assert Solution().countSmaller([5,2,6,1]) == [2,1,1,0]
assert Solution().countSmaller([7,1,3,2,9,2,1]) == [5,0,3,1,2,1,0]