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
import collections


class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        Facebook
        hashmap
        DFS
        T:O(n) S:O(n)
        Runtime: 12 ms, faster than 99.26% of Python online submissions for Nested List Weight Sum II.
        Memory Usage: 13 MB, less than 72.17% of Python online submissions for Nested List Weight Sum II.
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        level = collections.defaultdict(list)

        def dfs(weight, nestedList):
            if weight not in level:
                level[weight] = []
            for n in nestedList:
                if n.isInteger():
                    level[weight].append(n.getInteger())
                else:
                    dfs(weight + 1, n.getList())

        dfs(1, nestedList)
        ans = 0
        l = max(level.keys())
        for a in level:
            ans += sum(level[a]) * (l - a + 1)

        return ans




