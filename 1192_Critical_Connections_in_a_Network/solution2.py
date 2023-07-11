import collections
from typing import List


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        # 先構建一個圖，紀錄每個節點的鄰居
        self.node_neighbors = collections.defaultdict(list)
        for s, e in connections:
            self.node_neighbors[s].append(e)
            self.node_neighbors[e].append(s)

        # 構建一個陣列，紀錄每個節點的 id, -1 代表還沒有被訪問過
        self.node_id = [-1 for _ in range(n)]
        self.ans = []
        self.dfs(0, -1, 0)

        return self.ans

    def dfs(self, node: int, parent: int, id: int) -> int:
        # 先將當前節點的 id 設為 從父節點傳來的 id
        self.node_id[node] = id
        # 遍歷當前節點的鄰居
        for neighbor in self.node_neighbors[node]:
            # 假設鄰居是父節點，則跳過
            if neighbor == parent:
                continue
            # 如果鄰居還沒有被訪問過，則進行 dfs, 並取得鄰居的 id, 在與自身的 id 比較，取較小的那個
            elif self.node_id[neighbor] == -1:
                self.node_id[node] = min(
                    self.node_id[node], self.dfs(neighbor, node, id + 1)
                )
            # 如果鄰居已經被訪問過，則取鄰居的 id 與自身的 id 比較，取較小的那個
            else:
                self.node_id[node] = min(self.node_id[node], self.node_id[neighbor])

        # 若自身的id與父節點給予的id相同，代表自身與父節點之間沒有其他的連接，則自身與父節點為一個關鍵連接
        if id == self.node_id[node] and node != 0:
            self.ans.append([parent, node])

        # 回傳自身的 id
        return self.node_id[node]
