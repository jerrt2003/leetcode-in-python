class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        Stack + Mono-Q
        T:O(n) S:O(n)
        Runtime: 16 ms, faster than 95.39% of Python online submissions for Minimum Cost Tree From Leaf Values.
        Memory Usage: 12.8 MB, less than 43.16% of Python online submissions for Minimum
        https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/339959/One-Pass-O(N)-Time-and-Space
        :type arr: List[int]
        :rtype: int
        """
        stack = [float('inf')]
        res = 0
        for a in arr:
            while a >= stack[-1]:
                cur = stack.pop()
                res += min(a, stack[-1])*cur
            stack.append(a)
        while len(stack) > 2:
            cur = stack.pop()
            res += cur * stack[-1]
        return res

print Solution().mctFromLeafValues([6,2,4])

