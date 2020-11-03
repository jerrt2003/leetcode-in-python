class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        Stack
        T:O(n) S:O(n)
        Runtime: 60 ms, faster than 60.23% of Python online submissions for Validate Stack Sequences.
        Memory Usage: 12.8 MB, less than 64.19% of Python online submissions for Validate Stack Sequences.
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        # stack = []
        # i = 0
        # while pushed:
        #     stack.append(pushed.pop(0))
        #     while stack and stack[-1] == popped[i]:
        #         stack.pop()
        #         i += 1
        #
        # return len(stack) == 0

        """
        Stack
        T:O(n) S:O(n)
        Runtime: 60 ms, faster than 60.23% of Python online submissions for Validate Stack Sequences.
        Memory Usage: 12.8 MB, less than 64.19% of Python online submissions for Validate Stack Sequences.
        :type pushed: List[int]
        :type popped: List[int]        
        :rtype: bool
        """
        stack = []
        i = 0
        while pushed:
            stack.append(pushed.pop(0))
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return len(stack) == 0


print Solution().validateStackSequences([1,2,3,4,5],[4,5,3,2,1])