# -*- coding: utf-8 -*-
class Solution(object):

    def deleteNodesInNTree(self, root):
        self.res = []
        self.dfs(root, None)
        return self.res

    def dfs(self, node, parent):
        if not node:
            return
        for child in node.children:
            self.dfs(child, node)
        if node.val == 'B' and parent.val == 'R':
            node.children = None
            self.res.append(node)
