from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = [0]
        visited = set([0])
        while q:
            room_idx = q.pop(0)
            for key in rooms[room_idx]:
                if key not in visited:
                    visited.add(key)
                    q.append(key)
        return len(visited) == len(rooms)