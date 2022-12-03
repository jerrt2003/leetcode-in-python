from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
    # BFS 層序遍歷
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     ret: List[int] = []
    #     if not root:
    #         return ret
    #     q: List[TreeNode] = [root]
    #     while q:
    #         curr_node: TreeNode = TreeNode()
    #         for _ in range(len(q)):
    #             curr_node = q.pop(0)
    #             if curr_node.left:
    #                 q.append(curr_node.left)
    #             if curr_node.right:
    #                 q.append(curr_node.right)
    #         ret.append(curr_node.val)
    #     return ret

class Solution:
    # DFS
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret: List[int] = []
        level: int = 1
        self.helper(root, ret, level)
        return ret

    def helper(self, root:Optional[TreeNode], ret: List[int], level: int) -> None:
        if not root:
            return
        if len(ret) < level:
            ret.append(root.val)
        self.helper(root.right, ret, level+1)
        self.helper(root.left, ret, level+1)
