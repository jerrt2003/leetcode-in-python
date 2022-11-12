class Solution(object):
    def slidingPuzzle(self, board):
        """
        Facebook
        BFS
        T:O(V+E) S:O(V)
        Runtime: 32 ms, faster than 89.30% of Python online submissions for Sliding Puzzle.
        Memory Usage: 12.9 MB, less than 32.32% of Python online submissions for Sliding Puzzle.
        :type board: List[List[int]]
        :rtype: int
        """
        target = [1,2,3,4,5,0]
        start = board[0]+board[1]
        visit = set(tuple(start))
        q = [start]
        zero_dir = [[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]]
        ans = 0
        while q:
            l = len(q)
            for _ in range(l):
                curr = q.pop(0)
                if curr == target:
                    return ans
                else:
                    zero_idx = curr.index(0)
                    for nxt_zero_idx in zero_dir[zero_idx]:
                        tmp = curr[:]
                        tmp[nxt_zero_idx], tmp[zero_idx] = tmp[zero_idx], tmp[nxt_zero_idx]
                        if tuple(tmp) not in visit:
                            visit.add(tuple(tmp))
                            q.append(tmp)
            ans += 1
        return -1