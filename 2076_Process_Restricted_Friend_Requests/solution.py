import collections
from typing import List


class Solution:
    def friendRequests(
        self, n: int, restrictions: List[List[int]], requests: List[List[int]]
    ) -> List[bool]:
        self.n = n
        # 構造一個二維陣列，紀錄兩個人s,e是否有限制
        self.restriction = [[False for _ in range(n)] for _ in range(n)]
        for s, e in restrictions:
            # 限制是雙向的
            self.restriction[s][e] = True
            self.restriction[e][s] = True

        # 構造一個陣列，紀錄每個人的父節點
        self.parents = [i for i in range(n)]

        return [self.union(s, e) for s, e in requests]

    def find(self, i) -> None:
        # 假設 i 的父節點不是自己，則將 i 的父節點設為 i 的父節點的父節點(遞迴)
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i, j) -> bool:
        # 找到 i, j 的父節點 pi, pj
        pi, pj = self.find(i), self.find(j)
        # 若 i, j 的父節點相同(pi==pj) 則i, j在同一個集合中，代表可以成為朋友
        if pi == pj:
            return True
        else:
            # 若 pi != pj，則表示 i, j 不在同一個集合中，但是要檢查是否有限制
            # 若 pi, pj 沒有限制, 可以成為朋友 則將 pi 的父節點設為 pj 的父節點
            if not self.restriction[pi][pj]:
                self.parents[pi] = pj
                # 並將 pi 的所有限制添加到 pj 的限制中
                for k in range(self.n):
                    if self.restriction[pi][k]:
                        # 限制是雙向的
                        x = self.find(i)
                        self.restriction[pj][x] = True
                        self.restriction[x][pj] = True
                return True
            else:
                return False
