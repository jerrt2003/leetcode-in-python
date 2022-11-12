# -*- coding: utf-8 -*-
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        Solution: DFS
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/combination-sum/discuss/16510/Python-dfs-solution
        TP:
        - Using DFS
        - Read inline comment
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        candidates.sort()
        self.candidates = candidates
        self._dfs(target, 0, [])
        return self.res

    def _dfs(self, leftover, idx, path):
        '''
        :param leftover: 還剩下多少數字
        :param idx: 開始的idx
        :param path: 已知的path
        :return:
        '''
        if leftover < 0: # 假設leftover<0則表示我們沒有找到對的combination
            return
        if leftover == 0: # FOUND !!!
            self.res.append(path)
            return
        for i in range(idx, len(self.candidates)):
            # 下個iteration的leftover會是本次leftover - 本次數字
            self._dfs(leftover - self.candidates[i], i, path+[self.candidates[i]])

candidates = [2,3,6,7]
target = 7
sol = Solution()
print sol.combinationSum(candidates, target)

