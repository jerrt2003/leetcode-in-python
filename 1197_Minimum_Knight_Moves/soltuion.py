import collections


class Solution(object):
    def minKnightMoves(self, x, y):
        """
        BFS: Naive
        T:O(n) S:O(n)
        Runtime: 8328 ms, faster than 7.89% of Python online submissions for Minimum Knight Moves.
        Memory Usage: 58.6 MB, less than 100.00% of Python online submissions for Minimum Knight Moves.
        :type x: int
        :type y: int
        :rtype: int
        """
        # if (x, y) == (0, 0): return 0
        # visit = set((0, 0))
        # queue = [(0, 0, 0)]
        # while queue:
        #     curX, curY, lv = queue.pop(0)
        #     if (curX, curY) == (x, y):
        #         return lv
        #     for iDiff, jDiff in [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]:
        #         i, j = curX+iDiff, curY+jDiff
        #         if (i, j) not in visit:
        #             visit.add((i, j))
        #             queue.append((i, j, lv+1))
        if (x, y) == (0, 0): return 0
        x, y = abs(x), abs(y)
        queue = collections.deque([(0, 0, 0)])
        visit = set([(0, 0)])
        diff = [(2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]
        while queue:
            i, j, level = queue.popleft()
            if i == x and j == y:
                return level
            for diff_i, diff_j in diff:
                _i, _j = i + diff_i, j + diff_j
                if _i >= -1 and _j >= -1 and (_i, _j) not in visit:
                    visit.add((_i, _j))
                    queue.append((_i, _j, level + 1))

        return -1

print Solution().minKnightMoves(2, 1)