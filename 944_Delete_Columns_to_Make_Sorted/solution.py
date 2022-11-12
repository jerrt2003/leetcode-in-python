class Solution(object):
    def minDeletionSize(self, A):
        """
        T:O(n) S:O(n)
        Runtime: 104 ms, faster than 81.41% of Python online submissions for Delete Columns to Make Sorted.
        Memory Usage: 15.2 MB, less than 6.67% of Python online submissions for Delete Columns to Make Sorted.
        :type A: List[str]
        :rtype: int
        """
        ans = 0
        for col in [list(a) for a in zip(*A)]:
            col2 = sorted(col)
            if col != col2:
                ans += 1
        return ans

print Solution().minDeletionSize(["cba","daf","ghi"])
print Solution().minDeletionSize(["a","b"])
print Solution().minDeletionSize(["zyx","wvu","tsr"])