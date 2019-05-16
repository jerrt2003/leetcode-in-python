# -*- coding: utf-8 -*-
class NumArray(object):
    """
    Solution: FenwickTree
    Time Complexity:
    - init: O(nlog(n))
    - update: O(log(n))
    - sum: O(log(n))
    """

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.st = SegmentTree(nums)
        self.nums = nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        diff = val - self.nums[i]
        self.st.update(i+1, diff)
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.st.query(j+1) - self.st.query(i)

class SegmentTree(object):
    def __init__(self, nums):
        self.segmentTree = [0 for _ in range(len(nums)+1)]
        for i, j in enumerate(nums):
            self.update(i+1, j)

    def update(self, i, diff):
        while i < len(self.segmentTree):
            self.segmentTree[i] += diff
            i += self.lowbit(i)

    def query(self, i):
        sum = 0
        while i > 0:
            sum += self.segmentTree[i]
            i -= self.lowbit(i)
        return sum

    def lowbit(self, i):
        return i & -i

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)