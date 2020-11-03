class Solution(object):
    def shortestWay(self, source, target):
        """
        Greedy
        T:O(mn) S:O(m)
        Runtime: 52 ms, faster than 24.86% of Python online submissions for Shortest Way to Form String.
        Memory Usage: 12.9 MB, less than 100.00% of Python online submissions for Shortest Way to Form String.
        :type source: str
        :type target: str
        :rtype: int
        """
        pt2 = 0
        m,n = len(source),len(target)
        char_in_source = set(source)
        count = 0
        while pt2 < len(target):
            pt1 = 0
            while pt1 < m and pt2 < n:
                if target[pt2] not in char_in_source:
                    return -1
                if source[pt1] == target[pt2]:
                    pt1 += 1
                    pt2 += 1
                else:
                    pt1 += 1
            count += 1
        return count