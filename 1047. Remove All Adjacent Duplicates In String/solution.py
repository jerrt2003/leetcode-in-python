import collections


class Solution(object):
    def removeDuplicates(self, S):
        """
        Facebook
        Stack
        T:O(n) S:O(n)
        Runtime: 76 ms, faster than 54.61% of Python online submissions for Remove All Adjacent Duplicates In String.
        Memory Usage: 13.4 MB, less than 17.54% of Python online submissions for Remove All Adjacent Duplicates In String.
        :type S: str
        :rtype: str
        """
        stack = collections.deque([])
        for s in S:
            if not stack or s != stack[-1]:
                stack.append(s)
            else:
                stack.pop()
        return ''.join(stack)