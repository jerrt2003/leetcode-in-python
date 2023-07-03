import heapq
from typing import List


class Node:
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist_from_start = dist

    def __lt__(self, other):
        return self.dist_from_start < other.dist_from_start


class Solution:
    def shortestDistance(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> int:
        m, n = len(maze), len(maze[0])
        pq = [Node(start[0], start[1], 0)]
        heapq.heapify(pq)
        maze[start[0]][start[1]] = -1
        while len(pq) != 0:
            cur_node = heapq.heappop(pq)
            x, y, dist_from_start = cur_node.x, cur_node.y, cur_node.dist_from_start
            if [x, y] == destination:
                return dist_from_start

            for diff_x, diff_y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                next_x, next_y = x + diff_x, y + diff_y
                dist = dist_from_start + 1
                while (
                    0 <= next_x
                    and next_x < m
                    and 0 <= next_y
                    and next_y < n
                    and maze[next_x][next_y] != 1
                ):
                    next_x += diff_x
                    next_y += diff_y
                    dist += 1
                next_x -= diff_x
                next_y -= diff_y
                dist -= 1
                if maze[next_x][next_y] != -1:
                    maze[next_x][next_y] = -1
                    heapq.heappush(pq, Node(next_x, next_y, dist))

        return -1
