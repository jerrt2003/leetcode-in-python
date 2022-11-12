# -*- coding: utf-8 -*-
class Solution(object):
    def dailyTemperatures(self, T):
        """
        Solution: Stack
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MySELF!! (beat 99.10%)
        TP:
        - Initialize a list: res with 0
        - Then we use stack, this stack is to store the indices for T
        - Now we go through the T list and do following logic:
            if a T[i] < T[i+1]:
                T[i] = 1 (wait 1 day)
                !!! then we need to go back to check if T[i+1] also has higher temp. to previous non-decided days --> days in the stack
            else:
                we push this day to stack for future check.
        - (靈感) 升冪 降冪 排列
        :type T: List[int]
        :rtype: List[int]
        """
        m = len(T)
        res = [0 for _ in range(m)]
        stack = []
        i = 0
        while i+1 < m:
            if T[i] < T[i+1]:
                res[i] = 1
                while stack and T[i+1] > T[stack[-1]]:
                    idx = stack.pop()
                    res[idx] = (i+1) - idx
            else:
                stack.append(i)
            i += 1
        return res

#T = [73, 74, 75, 71, 69, 72, 76, 77, 76, 79]
#T = [4,3,2,4]
T = []
print Solution().dailyTemperatures(T)