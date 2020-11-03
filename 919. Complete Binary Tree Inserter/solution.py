# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter(object):

    def __init__(self, root):
        """
        BFS
        T:O(n) S:O(n)
        :type root: TreeNode
        """
        self.node_list = [root]
        idx = 0
        while True:
            curr_node = self.node_list[idx]
            if not curr_node.left and not curr_node.right:
                break
            if curr_node.left:
                self.node_list.append(curr_node.left)
            if curr_node.right:
                self.node_list.append(curr_node.right)
            idx += 1
        self.curr_idx = 0

    def insert(self, v):
        """
        T:O(n) S:O(1)
        Runtime: 44 ms, faster than 98.80% of Python online submissions for Complete Binary Tree Inserter.
        Memory Usage: 14.1 MB, less than 82.86% of Python online submissions for Complete Binary Tree Inserter.
        :type v: int
        :rtype: int
        """
        new_node = TreeNode(v, None, None)
        while self.node_list[self.curr_idx].left and self.node_list[self.curr_idx].right:
            self.curr_idx += 1
        if not self.node_list[self.curr_idx].left:
            self.node_list[self.curr_idx].left = new_node
        else:
            self.node_list[self.curr_idx].right = new_node
        self.node_list.append(new_node)
        return self.node_list[self.curr_idx].val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.node_list[0]

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()