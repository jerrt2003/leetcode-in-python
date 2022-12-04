from typing import List, Set, Tuple

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ret: List[List[int]] = []
        self.helper(sorted(candidates), [], target)
        return self.ret

    def helper(self, candidates: List[int], path: List[int], target: int) -> None:
        for i, c in enumerate(candidates):
            if sum(path) + c == target:
                self.ret.append(path + [c])
                break
            if sum(path) + c > target:
                break
            else:
                self.helper(candidates[i:], path+[c], target)