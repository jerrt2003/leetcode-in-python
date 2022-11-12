class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        T:O(V+E) S:O(V)
        Runtime: 44 ms, faster than 94.32% of Python online submissions for Keys and Rooms.
        Memory Usage: 13.5 MB, less than 25.52% of Python online submissions for Keys and Rooms.
        :type rooms: List[List[int]]
        :rtype: bool
        """
        access = [False for _ in range(len(rooms))]
        def dfs(i):
            if access[i]:
                return
            access[i] = True
            for nxt_room in rooms[i]:
                dfs(nxt_room)

        dfs(0)
        return all(access)

print Solution().canVisitAllRooms([[1],[2],[3],[]])
print Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]])