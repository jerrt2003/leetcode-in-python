# -*- coding: utf-8 -*-
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    """
    Solution: Stack
    Time Complexity: O(1)
    Space Complexity: O(h) *h is the height of the tree
    Inspired by: https://leetcode.com/problems/binary-search-tree-iterator/discuss/52526/Ideal-Solution-using-Stack-(Java)
    Algorithm:
    - we first create a stack to store all the left nodes
    - if len(stack) == 0, hasNext = False
    - As we traverse 'next' method, we start dealing/append right leaf nodes
    """

    class BSTIterator(object):
        """
        Solution: Stack
        Time Complexity: O(1)
        Space Complexity: O(h) *h is the height of the tree
        Inspired by: https://leetcode.com/problems/binary-search-tree-iterator/discuss/52526/Ideal-Solution-using-Stack-(Java)
        Algorithm:
        - we first create a stack to store all the left nodes
        - if len(stack) == 0, hasNext = False
        - As we traverse 'next' method, we start dealing/append right nodes
        """

        def __init__(self, root):
            """
            :type root: TreeNode
            """
            self.stack = list()
            cur = root
            while cur is not None:
                self.stack.append(cur)
                cur = cur.left

        def hasNext(self):
            """
            :rtype: bool
            """
            if len(self.stack) == 0:
                return False
            return True

        def next(self):
            """
            :rtype: int
            """
            node = self.stack.pop() # stack.pop()就會是最小的那個node
            cur = node
            # 開始處理右邊的node(假如有的話)
            if cur.right is not None:
                cur = cur.right
                self.stack.append(cur)
                while cur.left is not None: #左邊的node永遠會比一開始pop的node之父節點(stack的下一個node)來的小,所以需要加進去stack
                    cur = cur.left
                    self.stack.append(cur)
            return node.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())