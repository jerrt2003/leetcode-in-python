from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # return self.recursive(root)
        # return self.divide_conquer(root)
        return self.interactive(root)

    def recursive(self, root: Optional[TreeNode]) -> List[int]:
        ans: List[int] = []

        if not root:
            return ans
        
        def traversal(node: TreeNode, ans: List[int]) -> None:
            if node.left:
                traversal(node.left, ans)            
            ans.append(node.val)
            if node.right:
                traversal(node.right, ans)
            return

        traversal(root, ans)

        return ans

    def divide_conquer(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ret = []
        ret.extend(self.divide_conquer(root.left))
        ret.extend([root.val])
        ret.extend(self.divide_conquer(root.right))

        return ret

    def interactive(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if not root:
            return ret
        curr = root
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop(-1)
            ret.append(node.val)
            if node.right:
                curr = node.right
        return ret
