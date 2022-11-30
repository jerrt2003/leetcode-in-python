from typing import Optional, List, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        # self.stack = []
        # while root:
        #     self.stack.append(root)
        #     root = root.left
        self.stack: List[Tuple[TreeNode, int]] = [(root, 0)]


    def next(self) -> int:
        # curr = self.stack.pop()
        # ret = curr.val
        # curr = curr.right
        # while curr:
        #     self.stack.append(curr)
        #     curr = curr.left
        # return ret
        while True:
            node, color = self.stack.pop()
            if color == 1:
                return node.val
            else:
                if node.right:
                    self.stack.append((node.right, 0))
                self.stack.append((node, 1))
                if node.left:
                    self.stack.append((node.left, 0))

    def hasNext(self) -> bool:
        # return len(self.stack) != 0
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()