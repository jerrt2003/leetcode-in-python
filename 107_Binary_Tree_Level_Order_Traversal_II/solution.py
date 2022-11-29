from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # create a queue and push the root node into queue
        if not root:
            return []
        q = [root]
        # BFS, before pop from the queue, check how long the queue is
        # e.g. how many node in this level
        # retrieve the node value and put into ans of this level. 
        # at the end, attach this level ans to final ans
        ret = []
        while q:
            node_at_level = []
            node_count = len(q)
            for _ in range(node_count):
                node = q.pop(0)
                node_at_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ret.append(node_at_level)
        
        return ret[::-1]

        # reverse the final answer