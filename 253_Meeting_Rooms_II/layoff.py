import heapq

from typing import List

# intervals.sort(key=lambda x: x[0])：Python 中的 Timsort 排序算法時間複雜度為 O(N log N)，其中 N 是 intervals 中的間隔數量。
# 在 for 迴圈中，我們遍歷每個間隔，並根據條件將其加入或從優先級佇列中移出。Python 的 heapq 實現是一個二元堆，因此 push 和 pop 操作的時間複雜度都是 O(log K)，其中 K 是堆的大小。在最壞的情況下，所有的間隔都會被加入到堆中，因此 K <= N，所以這部分的總時間複雜度為 O(N log N)。
# 因此，整個函數的時間複雜度為 O(N log N) + O(N log N) = O(N log N)。請注意，這是在考慮最壞情況的情況下得到的時間複雜度。實際上，如果間隔的結束時間較早或者堆的大小較小，那麼實際的運行時間可能會更快。


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        pq: List[int] = []
        heapq.heapify(pq)
        for s, e in intervals:
            if len(pq) == 0:
                heapq.heappush(pq, e)
            else:
                if s < pq[0]:
                    heapq.heappush(pq, e)
                else:
                    heapq.heappushpop(pq, e)
        return len(pq)
