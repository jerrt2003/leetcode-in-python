# -*- coding: utf-8 -*-
class Solution(object):
    def depthSum(self, nestedList):
        """
        Solution: DFS
        Time Complexity:
        Space Complexity:
        TP:
        - Using DFS and for each level recursion pass in its level
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        return self.sum(nestedList, 1)

    def sum(self, curr_list, depth):
        """
        To return then sum for current list
        :param list:
        :param depth:
        :return:
        """
        res = 0
        for item in curr_list:
            if isinstance(item, int):
                res += depth*item
            elif isinstance(item, list):
                res += self.sum(item, depth+1)
        return res

input = [1,[4,[6]]]
sol = Solution()
print sol.depthSum(input)