class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        Facebook
        T:O(nlogn) S:O(n)
        Runtime: 24 ms, faster than 81.68% of Python online submissions for Construct Binary Search Tree from Preorder Traversal.
        Memory Usage: 12.7 MB, less than 81.46% of Python online submissions for Construct Binary Search Tree from Preorder Traversal.
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        curr = preorder[0]
        node = TreeNode(val=curr)
        preorder = preorder[1:]
        l, r = 0, len(preorder)
        while l < r:
            mid = (l+r-1)/2
            if preorder[mid] > curr:
                r = mid
            else:
                l = mid+1
        node.left = self.bstFromPreorder(preorder[:l])
        node.right = self.bstFromPreorder(preorder[l:])

        return node