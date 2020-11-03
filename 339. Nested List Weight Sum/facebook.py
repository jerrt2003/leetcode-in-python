# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum(self, nestedList):
        """
        Facebook
        DFS
        T:O(n) S:O(n)
        Runtime: 20 ms, faster than 78.95% of Python online submissions for Nested List Weight Sum.
        Memory Usage: 12.9 MB, less than 99.22% of Python online submissions for Nested List Weight Sum.
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def dfs(weight, nestedList):
            ans = 0
            for n in nestedList:
                if n.isInteger():
                    ans += weight * n.getInteger()
                else:
                    ans += dfs(weight + 1, n.getList())
            return ans

        return dfs(1, nestedList)