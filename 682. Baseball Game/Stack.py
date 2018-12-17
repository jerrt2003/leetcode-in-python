# -*- coding: utf-8 -*-
class Solution(object):
    def calPoints(self, ops):
        """
        Solution: Stack
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MySELF!!
        :type ops: List[str]
        :rtype: int
        """
        score = []
        for op in ops:
            try:
                op = int(op)
                score.append(int(op))
            except:
                if op == 'C':
                    if score:
                        score.pop()
                elif op == '+':
                    if len(score) < 2:
                        return 0
                    else:
                        tmp = score[-1] + score[-2]
                        score.append(tmp)
                elif op == 'D':
                    if score:
                        tmp = score[-1]*2
                        score.append(tmp)
        res = 0
        for s in score:
            res += s
        return res

ops = ["5","-2","4","C","D","9","+","+"]
print Solution().calPoints(ops)