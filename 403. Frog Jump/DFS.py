# -*- coding: utf-8 -*-
class Solution(object):
    def canCross(self, stones):
        """
        Solution: DFS + memorization
        Time Complexity: O(2^n)
        Space Complexity: O(n)
        Perf: TLE
        :type stones: List[int]
        :rtype: bool
        """
        DP = dict()
        def dfs(prev_pos, prev_jump):
            curr_pos = prev_pos + prev_jump
            if curr_pos == stones[-1]:
                return True
            if curr_pos not in set(stones) or curr_pos > stones[-1] or prev_jump == 0:
                return False
            if (curr_pos, prev_jump) in DP.keys():
                return DP[(curr_pos, prev_jump)]
            if not dfs(curr_pos, prev_jump+1) and not dfs(curr_pos, prev_jump-1) and not dfs(curr_pos, prev_jump):
                DP[(curr_pos, prev_jump)] = False
                return False
            return True

        return dfs(stones[0], 1)

#stones = [0,1,3,5,6,8,12,17]

stones = [0,2]

print Solution().canCross(stones)