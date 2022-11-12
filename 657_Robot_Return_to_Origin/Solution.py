# -*- coding: utf-8 -*-
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        L = R = U = D = 0
        for move in moves:
            if move == 'L': L+=1
            elif move == 'R': R+=1
            elif move == 'U': U+=1
            else: D+=1
        if L == R and U == D:
            return True
        return False

moves = "LL"
sol = Solution()
print sol.judgeCircle(moves)