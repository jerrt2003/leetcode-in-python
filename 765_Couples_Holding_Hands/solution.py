class Solution(object):
    def minSwapsCouples(self, row):
        """
        T:O(n^2) S:O(1)
        Runtime: 24 ms, faster than 43.75% of Python online submissions for Couples Holding Hands.
        Memory Usage: 12.7 MB, less than 89.90% of Python online submissions for Couples Holding Hands.
        :type row: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(0, len(row), 2):
            x = row[i]
            if row[i+1] == x^1: continue
            ans += 1
            for j in range(i+1, len(row)):
                if row[j] == x^1:
                    row[i+1],row[j] = row[j],row[i+1]
                    break
        return ans