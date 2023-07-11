# Union Find
from typing import List

# 這段程式碼使用並查集（Union-Find）資料結構來找到一個無向圖中的冗餘連接，也就是在一棵樹中形成迴圈的邊。問題假設該無向圖所有的邊都形成一棵樹，但多出一條邊造成迴圈。我們要找出這條造成迴圈的邊。
# 這個演算法的時間複雜度是 O(n)，空間複雜度是 O(n)，其中 n 是邊的數量


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 我們用一個列表 parent 來追蹤每個節點的父節點。一開始，每個節點的父節點就是它自己
        self.parent = [i for i in range(len(edges) + 1)]
        ans = None
        # 接著，我們遍歷每一條邊，對於每一條邊的兩個節點 s 和 e，我們呼叫 union(s, e)。
        # 這個函式會找到 s 和 e 的父節點 px 和 py，如果 px 和 py 相等，那麼 s 和 e 在同一個集合中，這表示我們找到了造成迴圈的邊。
        # 否則，我們將 px 的父節點設為 py，將 s 和 e 合併到同一個集合中。
        for s, e in edges:
            if self.union(s, e):
                ans = [s, e]
        return ans

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return True
        self.parent[px] = py
        return False
