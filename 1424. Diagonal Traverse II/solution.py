class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        T: O(n), S:O(n)
        Runtime: 952 ms, faster than 97.04% of Python online submissions for Diagonal Traverse II.
        Memory Usage: 34.9 MB, less than 100.00% of Python online submissions for Diagonal Traverse II.
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        res = []
        for i, a in enumerate(nums):
            for j, b in enumerate(a):
                if len(res) <= i+j:
                    res.append([])
                res[i+j].append(b)
        return [a for r in res for a in reversed(r)]