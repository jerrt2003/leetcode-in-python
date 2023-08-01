import collections
import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # 將在相同時間開始的 events 的結束時間放到一個 list 裡
        events_start_at_i = collections.defaultdict(list)
        for s, e in events:
            events_start_at_i[s].append(e)

        ans = 0
        pq = []
        # 遍歷所有時間點
        for i in range(1, 10**5 + 1):
            # 將在當前時間點 i 開始的 events 的結束時間放到 heap 裡
            for j in events_start_at_i[i]:
                heapq.heappush(pq, j)

            while pq:
                # 若是 event的結束時間小於當前時間點 i，則 pop 掉(代表無法參加)
                _end = heapq.heappop(pq)
                if _end < i:
                    continue
                else:
                    # 否則參加該 event，並且 ans + 1
                    ans += 1
                    break

        return ans
