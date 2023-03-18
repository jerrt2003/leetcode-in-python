# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from common.tree_node import TreeNode
from typing import List

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        # 先用 BFS 把 tree 走一遍，把每個 node 的值都存起來
        ans: List[int] = []
        queue = [root]
        while len(queue) != 0:
            node = queue.pop(0)
            if not node:
                ans.append("X")
                continue
            ans.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        # 把 list 轉成 string
        # 此時的 ans 會是 [root -> left -> right] 的順序
        return ",".join(ans)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(",")
        node = TreeNode(val=int(data[0]))
        queue = [node]
        i = 0
        while len(queue) != 0:
            cur_node = queue.pop(0)
            cur_node.left = None if data[i+1] == "X" else TreeNode(val=int(data[i+1]))
            if cur_node.left:
                queue.append(cur_node.left)
            i+=1
            cur_node.right = None if data[i+1] == "X" else TreeNode(val=int(data[i+1]))
            if cur_node.right:
                queue.append(cur_node.right)
            i+=1

        return node
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))