class Solution(object):
    def removeDuplicates(self, s, k):
        """
        T:O(n) S:O(n)
        Runtime: 52 ms, faster than 85.45% of Python online submissions for Remove All Adjacent Duplicates in String II.
        Memory Usage: 14.4 MB, less than 100.00% of Python online submissions for Remove All Adjacent Duplicates in String II.
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        for c in s:
            if not stack or c != stack[-1][0]:
                stack.append([c, 1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
        return ''.join(c*k for c, k in stack)




print Solution().removeDuplicates("deeedbbcccbdaa",3)
print Solution().removeDuplicates('pbbcggttciiippooaais',2)