import collections
import heapq

from sys import maxsize
from typing import List, Dict, Tuple


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # return self.bfs(maze, start, destination)
        return self.dijkstra(maze, start, destination)


    def bfs(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # create a queue, put init pos into the queue with dist as 0
        # e.g. [1,2,0] -> start pos is [1, 2] with dist of 0
        # create an hashmap to record min path to given pos
        q: List[List[int]] = [start + [0]]
        maze[start[0]][start[1]] = 2
        pos_min_path: Dict[Set[int], int] = collections.defaultdict(int)
        pos_min_path[(start[0], start[1])] = 0

        # BFS, pop ball pos from queue and find all it's possible next pos
        while q:
            q_length = len(q)
            for _ in range(q_length):
                pos = q.pop(0)
                next_pos_list = self.find_next_pos(pos, maze, pos_min_path)
                q.extend(next_pos_list)

        # return -1 if not found or return dist
        if (destination[0], destination[1]) not in pos_min_path.keys():
            return -1
        else:
            return pos_min_path[(destination[0], destination[1])]        

    def find_next_pos(self, pos: List[int], maze: List[List[int]], pos_min_path: Dict[List[int], int]) -> List[List[int]]:
        ret: List[List[int]] = []
        directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
        for x, y in directions:
            i, j, dist = pos[0], pos[1], pos[2]
            row = x + i
            col = y + j
            dist += 1
            while 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != 1:
                row += x
                col += y
                dist += 1
            row -= x
            col -= y
            dist -= 1
            # if current pos dist is smaller than we found so far, then put into the queue, otherwise disregard it (prune)
            if (row, col) not in pos_min_path.keys() or dist < pos_min_path[(row, col)]:
                pos_min_path[(row, col)] = dist
                ret.append([row, col, dist])
        return ret

    def dijkstra(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # create an priority queue and push init pos into queue
        # create an hashmap to record 'visited' node and its shortest path
        self.shortest_path: Dict[Tuple[int], int] = collections.defaultdict(int)
        i, j = start[0], start[1]
        q: List[Tuple[int, Tuple[int]]] = [(0, (i, j))]
        heapq.heapify(q)
        # BFS start, pop the node from pq
        # mark the popped node into hashmap with it's shortest path
        # (if node is destination, then just return the shortest path)
        # visited node all neighbors
        # if neighbor already in hashmap, disgard it (shortest path already found)
        # push neighbors into pq with updated distance
        while q:
            node_meta = heapq.heappop(q)
            dist, cords = node_meta[0], node_meta[1]
            if cords == tuple(destination):
                return dist
            self.shortest_path[cords] = dist
            self.dijkstra_find_next_pos(dist, cords, q, maze)

        return -1

    def dijkstra_find_next_pos(self, dist: int, cords: Tuple[int], q: List[Tuple[int, Tuple[int]]], maze: List[List[int]]) -> None:
        for x, y in [[1, 0],[-1, 0],[0, 1],[0, -1]]:
            path_dist = dist
            i, j = cords[0], cords[1]
            i += x
            j += y
            path_dist += 1
            while 0 <= i < len(maze) and 0 <= j < len(maze[0]) and maze[i][j] != 1:
                i += x    
                j += y
                path_dist += 1
            i -= x
            j -= y
            path_dist -= 1
            if (i, j) not in self.shortest_path.keys():
                heapq.heappush(q, (path_dist, (i, j)))
            

