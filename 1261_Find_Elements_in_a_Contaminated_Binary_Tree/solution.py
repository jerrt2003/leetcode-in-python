# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements(object):

    def __init__(self, root):
        """
        Recover: T:O(n) S:O(n)
        Find: T:O(1) S:O(1)
        Runtime: 88 ms, faster than 53.37% of Python online submissions for Find Elements in a Contaminated Binary Tree.
        Memory Usage: 19.5 MB, less than 100.00% of Python online submissions for Find Elements in a Contaminated Binary Tree.
        :type root: TreeNode
        """
        self.nodeValue = set()
        root.val = 0
        self.recover(root)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.nodeValue

    def recover(self, root):
        self.nodeValue.add(root.val)
        if root.left != None:
            root.left.val = 2*root.val+1
            self.recover(root.left)
        if root.right != None:
            root.right.val = 2*root.val+2
            self.recover(root.right)

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)