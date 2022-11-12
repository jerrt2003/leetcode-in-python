class Solution(object):
    def canCross(self, stones):
        """
        T:O(n^2)
        S:O(n^2)
        Perf: Runtime: 228 ms, faster than 52.74% / Memory Usage: 13.5 MB, less than 80.95%
        :type stones: List[int]
        :rtype: bool
        """
        DP = {stone: set() for stone in stones}
        DP[0].add(0)
        for stone in stones:
            if stone in DP:
                for j in DP[stone]:
                    for jump in (j - 1, j, j + 1):
                        next_pos = stone + jump
                        if next_pos == stones[-1]:
                            return True
                        elif next_pos > stone and next_pos in DP:
                            DP[next_pos].add(jump)
        return len(DP[stones[-1]]) > 0


stones = [0,1,3,5,6,8,12,17]
assert Solution().canCross(stones) == True