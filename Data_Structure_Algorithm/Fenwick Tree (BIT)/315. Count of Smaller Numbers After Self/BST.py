# -*- coding: utf-8 -*-
class Solution(object):
    def countSmaller(self, nums):
        """
        Sol: BST
        Time: O(nlog(n)) (worst: O(n^2)
        Space: O(k) k is distinct elements
        Perf: Runtime: 180 ms, faster than 37.71% / Memory Usage: 16.4 MB, less than 35.98%
        :type nums: List[int]
        :rtype: List[int]
        """
        def insert(node, val):
            if node.val == val:
                node.count += 1
                return node.leftCount
            elif node.val < val:
                if not node.right:
                    node.right = BST(val)
                    return node.smaller()
                return node.smaller() + insert(node.right, val)
            else:
                node.leftCount += 1
                if not node.left:
                    node.left = BST(val)
                    return 0
                return insert(node.left, val)

        root = BST(nums[-1])
        res = [0]
        for num in nums[:-1][::-1]:
            res.append(insert(root, num))
        return res[::-1]

class BST(object):
    def __init__(self, val):
        self.val = val
        self.count = 1
        self.leftCount = 0
        self.left = None
        self.right = None

    def smaller(self):
        return self.count + self.leftCount


assert Solution().countSmaller([5,2,6,1]) == [2,1,1,0]