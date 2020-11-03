class Solution(object):
    def findParent(self, n, query):
        def _findParent(root, n, target, parent):
            if root == target:
                return parent
            elif target <= root-(1<<(n-1)):
                return _findParent(root-(1<<(n-1)),n-1,target,root)
            else:
                return _findParent(root-1,n-1,target,root)

        res = []
        root = (1<<n)-1
        for q in query:
            res.append(_findParent(root, n, q, -1))
        return res

assert Solution().findParent(3, [1,3,6,7])