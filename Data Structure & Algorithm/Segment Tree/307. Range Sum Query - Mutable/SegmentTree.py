# -*- coding: utf-8 -*-
class NumArray(object):

    def __init__(self, nums):
        """
        Perf: Runtime: 220 ms, faster than 41.88% / Memory Usage: 26.8 MB, less than 18.52%
        :type nums: List[int]
        """
        start, end = 0, len(nums)-1
        self.nums = nums
        self.root = self._buildTree(start, end, nums)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        delta = val - self.nums[i]
        self.nums[i] = val
        self._update(self.root, i, delta)

    def _update(self, node, i, delta):
        if node.start == node.end == i:
            node.val += delta
            return
        mid = (node.start+node.end) // 2
        if i <= mid:
            self._update(node.left, i, delta)
        else:
            self._update(node.right, i, delta)
        node.val = node.left.val + node.right.val
        return

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._sumRange(self.root, i, j)

    def _sumRange(self, node, i, j):
        if node.start == i and node.end == j:
            return node.val
        mid = (node.start+node.end) // 2
        if j <= mid:
            return self._sumRange(node.left, i, j)
        elif i > mid:
            return self._sumRange(node.right, i, j)
        else:
            return self._sumRange(node.left, i, mid) + self._sumRange(node.right, mid+1, j)


    def _buildTree(self, start, end, nums):
        """
        to build a segment tree
        :param nums:
        :return: SegTreeNode
        """
        if start == end:
            return SegTreeNode(start, end, nums[start])
        mid = (start+end) / 2
        left = self._buildTree(start, mid, nums)
        right = self._buildTree(mid+1, end, nums)
        return SegTreeNode(start, end, left.val+right.val, left=left, right=right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

class SegTreeNode(object):
    def __init__(self, start, end, val, left=None, right=None):
        self.start = start
        self.end = end
        self.val = val
        self.left = left
        self.right = right


numArray = NumArray([1, 3, 5])
assert numArray.sumRange(0, 1) == 4
numArray.update(1,2)