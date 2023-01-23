from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = {start}
        queue = [start]
        while len(queue) != 0:
            idx = queue.pop(0)
            if arr[idx] == 0:
                return True
            next_indices = []
            if idx + arr[idx] < len(arr):
                next_indices.append(idx+arr[idx])
            if idx - arr[idx] >= 0:
                next_indices.append(idx-arr[idx])
            for i in next_indices:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
        return False
