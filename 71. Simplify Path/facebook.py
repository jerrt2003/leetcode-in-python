class Solution(object):
    def simplifyPath(self, path):
        """
        Facebook
        T:O(n) S:O(n)
        Runtime: 24 ms, faster than 72.80% of Python online submissions for Simplify Path.
        Memory Usage: 12.8 MB, less than 45.28% of Python online submissions for Simplify Path.
        :type path: str
        :rtype: str
        """
        path = [p for p in path.split('/') if p != '.' and p != '']
        stack = []
        for p in path:
            if p != '..':
                stack.append(p)
            elif p == '..' and stack:
                stack.pop()

        return '/' + '/'.join(stack)