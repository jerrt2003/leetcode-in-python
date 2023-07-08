from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        stack = []
        i = 0
        cur_num = ""
        while i < len(s):
            if s[i].isdigit() or s[i] == "-":
                cur_num += s[i]
            else:
                if cur_num:
                    val = int(cur_num)
                    cur_num = ""
                    new_node = TreeNode(val=val)
                    if stack:
                        if not stack[-1].left:
                            stack[-1].left = new_node
                        else:
                            stack[-1].right = new_node
                    stack.append(new_node)
                if s[i] == ")":
                    stack.pop()
            i += 1

        if cur_num:
            return TreeNode(val=int(cur_num))

        return None if not stack else stack[-1]
