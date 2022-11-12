# -*- coding: utf-8 -*-
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.root = self._buildTree(0, len(nums)-1, nums)

    def _buildTree(self, start, end, nums):
        if start == end:
            return SegTreeNode(start, end, nums[start])
        mid = (start+end) // 2
        left = self._buildTree(start, mid, nums)
        right = self._buildTree(mid+1, end, nums)
        return SegTreeNode(start, end, max(left.rangeMax, right.rangeMax), left=left, right=right)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.nums[i] = val
        self._update(self.root, i, val)

    def _update(self, node, i, val):
        if node.start == node.end == i:
            node.rangeMax = val
            return
        mid = (node.start+node.end) // 2
        if i <= mid:
            self._update(node.left, i, val)
        else:
            self._update(node.right, i, val)
        node.rangeMax = max(node.left.rangeMax, node.right.rangeMax)

    def maxRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._maxRange(self.root, i, j)

    def _maxRange(self, node, i, j):
        if node.start == i and node.end == j:
            return node.rangeMax
        mid = (node.start + node.end) // 2
        if j <= mid:
            return self._maxRange(node.left, i, j)
        elif i > mid:
            return self._maxRange(node.right, mid+1, j)
        else:
            return max(self._maxRange(node.left, i, mid), self._maxRange(node.right, mid+1, j))

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

class SegTreeNode(object):
    def __init__(self, start, end, rangeMax, left=None, right=None):
        self.start = start
        self.end = end
        self.rangeMax = rangeMax
        self.left = left
        self.right = right

numArray = NumArray([1, 10, 5, 7, 9, 2])
assert numArray.maxRange(0, 1) == 10
numArray.update(0, 11)
assert numArray.maxRange(0, 1) == 11
assert numArray.maxRange(0, 5) == 11