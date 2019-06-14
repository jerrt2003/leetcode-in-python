# -*- coding: utf-8 -*-
'''
class TreeNode(object):
    def __init__(self, parent, data):
        self.parent = parent
        self.data = data
'''

class Solution(object):
    def deleteSingleNode(self, treeList, target):
        i = 0
        while i < len(treeList):
            if treeList[i].data == target:
                break
            i += 1
        parent_idx = treeList[i].parent
        res = []
        for j in range(len(treeList)):
            if j < i:
                res.append(treeList[j])
            elif j > i:
                pi = treeList[j].parent
                if pi < parent_idx:
                    res.append(treeList[j])
                elif pi == i:
                    res.append(TreeNode(parent_idx, treeList[j].data))
                else:
                    res.append(TreeNode(pi-1, treeList[j].data))
        return res


