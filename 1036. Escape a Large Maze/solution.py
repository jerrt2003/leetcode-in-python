import collections


class Solution(object):
    def isEscapePossible(self, blocked, source, target):
        """
        BFS
        T:O(2B^B) S:O(2B^B)
        Runtime: 4720 ms, faster than 6.15% of Python online submissions for Escape a Large Maze.
        Memory Usage: 57.2 MB, less than 6.25% of Python online submissions for Escape a Large Maze.
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """
        if not blocked:
            return True
        blocked = set(map(tuple, blocked))
        def bfs(si, sj, ti, tj):
            visit = set()
            visit.add((si, sj))
            queue = collections.deque([(si, sj)])
            step = 0
            while queue:
                l = len(queue)
                for _ in range(l):
                    curr = queue.popleft()
                    i, j = curr[0], curr[1]
                    if (i, j) == (ti, tj):
                        return True
                    for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                        if 0 <= x < 10**6 and 0 <= y < 10**6 and (x, y) not in blocked and (x, y) not in visit:
                            visit.add((x, y))
                            queue.append((x, y))
                step += 1
                if step == len(blocked)*2:
                    return True
            return False

        return bfs(source[0],source[1],target[0],target[1]) and bfs(target[0],target[1],source[0],source[1])