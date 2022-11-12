class Solution(object):
    def backspaceCompare(self, S, T):
        """
        Facebook
        T:O(n) S:O(n)
        Runtime: 20 ms, faster than 76.66% of Python online submissions for Backspace String Compare.
        Memory Usage: 12.9 MB, less than 5.56% of Python online submissions for Backspace String Compare.
        :type S: str
        :type T: str
        :rtype: bool
        """

        def finalString(s):
            stack = []
            for _s in s:
                if _s.isalpha():
                    stack.append(_s)
                else:
                    if stack:
                        stack.pop()
            return ''.join(stack)

        return finalString(S) == finalString(T)

print Solution().backspaceCompare("ab#c","ad#c")