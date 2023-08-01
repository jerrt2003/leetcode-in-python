from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l, r = 0, max(citations) + 1
        while l < r:
            mid = (l + r - 1) // 2
            if not self.check(mid, citations):
                r = mid
            else:
                l = mid + 1
        return l - 1

    def check(self, mid: int, citations: List[int]) -> bool:
        count = 0
        for citation in citations:
            if citation >= mid:
                count += 1
            if count >= mid:
                return True
        return count >= mid
