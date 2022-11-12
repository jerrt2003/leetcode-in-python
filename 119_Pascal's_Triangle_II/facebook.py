class Solution(object):
    def getRow(self, rowIndex):
        """
        Facebook
        T:O(n^2) S:O(n)
        Runtime: 16 ms, faster than 92.17% of Python online submissions for Pascal's Triangle II.
        Memory Usage: 12.8 MB, less than 30.37% of Python online submissions for Pascal's Triangle II.
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1] * (rowIndex+1)
        for i in range(2, rowIndex+1):
            for j in range(i-1, 0, -1):
                row[j] += row[j-1]
        return row