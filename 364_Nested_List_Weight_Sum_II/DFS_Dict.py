# -*- coding: utf-8 -*-
#class NestedInteger(object):
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
    def depthSumInverse(self, nestedList):
        """
        Solution: DFS + Dict(hashtable)
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MySELF!!
        TP:
        - use a dict (or hashtable in java) to store the k(level) and v(values)
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if nestedList is None or len(nestedList) == 0: return 0
        self.depth_table = dict()
        self.helper(nestedList, 1)
        total_level = len(self.depth_table.keys())
        res = 0
        for k, v in self.depth_table.iteritems():
            curr_total = 0
            for _v in v:
                curr_total += _v
            res += (total_level - k + 1)*curr_total
        return res

    def helper(self, curr_list, curr_level):
        if not self.depth_table.has_key(curr_level):
            self.depth_table[curr_level] = []
        for item in curr_list:
            if isinstance(item, int):
                self.depth_table[curr_level].append(item)
            else:
                self.helper(item, curr_level+1)


nestedList = [[[8],4]]
sol = Solution()
print sol.depthSumInverse(nestedList)