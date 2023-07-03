from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.candidates = sorted(candidates)
        self.target = target
        cur_sum = 0
        cur_path = []
        self.dfs(cur_sum, cur_path, 0)

        return self.ans

    def dfs(self, cur_sum: int, cur_path: List[int], idx):
        if idx == len(self.candidates):
            return

        for i in range(idx, len(self.candidates)):
            if i != idx and self.candidates[i] == self.candidates[i - 1]:
                continue
            if cur_sum + self.candidates[i] > self.target:
                break
            elif cur_sum + self.candidates[i] == self.target:
                self.ans.append(cur_path + [self.candidates[i]])
                break
            else:
                self.dfs(
                    cur_sum + self.candidates[i], cur_path + [self.candidates[i]], i + 1
                )
