# -*- coding: utf-8 -*-
class Solution(object):
    def getRow(self, rowIndex):
        """
        Solution: BFS
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MySELF!! (24ms, beat 22.39%)
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0: return [1]
        stack = [1]
        i = 0
        while i < rowIndex:
            m = len(stack)
            prev = 0
            for _ in range(m):
                cur = stack.pop(0)
                stack.append(prev + cur)
                prev = cur
            stack.append(1)
            i += 1
        return stack