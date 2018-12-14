# -*- coding: utf-8 -*-
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Solution: DFS
        Time Complexity:
        Space Complexity:
        Inspired By: MySELF!!
        TP:
        - this solution is to flatten the list during init, which is not what question is asking for...DON'T USE THIS SOLUTION (even it pass)
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.res = []
        self.retreiveList(nestedList)
        print self.res

    def retreiveList(self, nestedList):
        for item in nestedList:
            if item.isInteger():
                self.res.append(item.getInteger())
            else:
                self.retreiveList(item.getList())

    def next(self):
        """
        :rtype: int
        """
        return self.res.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.res:
            return False
        else:
            return True