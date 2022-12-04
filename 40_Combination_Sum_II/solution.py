from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ret: List[List[int]] = []
        self.helper(sorted(candidates), target, [])
        return self.ret


    def helper(self, candidates: List[int], target: int, path: List[int]) -> None:
        for i, v in enumerate(candidates):
            if v + sum(path) == target:
                self.ret.append(path+[v])
                break
            elif v + sum(path) > target:
                break
            else:
                # 同一层数值相同的结点第 2、3 ... 个结点，因为数值相同的第 1 个结点
                # 已经搜索出了包含了这个数值的全部结果，同一层的其它结点，候选数的个数更少，
                # 搜索出的结果一定不会比第 1 个结点更多，并且是第 1 个结点的子集
                if i-1 >= 0 and candidates[i-1] == candidates[i]:
                    continue
                self.helper(candidates[i+1:], target, path+[v])