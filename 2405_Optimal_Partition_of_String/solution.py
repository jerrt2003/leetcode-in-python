class Solution:
    def partitionString(self, s: str) -> int:
        if not s:
            return 0
        visited = set([])
        ans = 1
        for _s in s:
            if _s in visited:
                ans += 1
                visited = set([])
            visited.add(_s)
        return ans
