# -*- coding: utf-8 -*-
class Solution(object):
    def oddEvenJumps(self, A):
        """
        Solution: DP + Stack
        Time Complexity: O(nlog(n))
        Space Complexity: O(n)
        Perf: Runtime: 176 ms, faster than 80.92% / Memory Usage: 14 MB, less than 70.15%
        Inspired By:
        - https://leetcode.com/problems/odd-even-jump/solution/
        - https://www.youtube.com/watch?v=MEqDu4hA_Wo&t=1159s
        - https://leetcode.com/problems/odd-even-jump/discuss/217981/JavaC++Python-DP-idea-Using-TreeMap-or-Stack
        :type A: List[int]
        :rtype: int
        """
        m = len(A)

        def generateNextStep(ordered_idx):
            ret = [None for _ in range(m)]
            stack = []
            for idx in ordered_idx:
                while stack and idx > stack[-1]:
                    ret[stack.pop()] = idx
                stack.append(idx)
            return ret

        B = sorted(range(m), key=lambda i: A[i])
        oddNext = generateNextStep(B)
        B.sort(key=lambda i: -A[i])
        evenNext = generateNextStep(B)

        odd = [0 for _ in range(m)]
        even = [0 for _ in range(m)]
        odd[-1] = 1
        even[-1] = 1
        for i in range(m-2, -1, -1):
            if oddNext[i] is not None:
                odd[i] = even[oddNext[i]]
            if evenNext[i] is not None:
                even[i] = odd[evenNext[i]]

        return sum(odd)