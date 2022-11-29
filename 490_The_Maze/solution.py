from typing import List

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        return self.bfs(maze, start, destination)

    def bfs(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        def find_next_pos(i: int, j: int) -> List[List[int]]:
            directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
            pos_list: List[List[int]] = []
            for x, y in directions:
                row, col = i+x, j+y # start with next pos
                while 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != 1:
                    row += x
                    col += y
                row -= x # already hit a wall, revert the pos to preivous one (i.e. pos where ball stop)
                col -= y
                if maze[row][col] != 2:
                    maze[row][col] = 2
                    pos_list.append([row, col])
            return pos_list

        # mark init pos 'visited' then put init pos into q
        maze[start[0]][start[1]] = 2
        q = [start]
        # pop ball location, if it's destination, return True
        # if not, check it's next possible pos, mark it then push into queue
        while q:
            i, j = q.pop(0)
            if [i, j] == destination:
                return True
            else:
                q.extend(find_next_pos(i, j))

        # return False if no answer if found
        return False