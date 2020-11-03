class Solution(object):
    def maxArea(self, height):
        """
        Facebook
        2 pointer
        T:O(n) S:O(1)
        Runtime: 108 ms, faster than 70.05% of Python online submissions for Container With Most Water.
        Memory Usage: 14 MB, less than 21.53% of Python online submissions for Container With Most Water.
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        ans = 0
        while i < j:
            if height[i] < height[j]:
                ans = max(ans, (height[i] * (j - i)))
                i += 1
            else:
                ans = max(ans, (height[j] * (j - i)))
                j -= 1
        return ans

