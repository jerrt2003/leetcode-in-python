from typing import List, Tuple, Set

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # find init color
        # create a queue and place init point into queue
        # create a SET to record 'visited' nodes
        init_color = image[sr][sc]
        q: List[Tuple[int]] = [(sr, sc)]
        visited: Set[Tuple[int]] = {(sr, sc)}

        # BFS, pop node from queue
        # change color then check all its neighbor
        # if neighbor not visited, put into SET and push into queue
        image[sr][sc] = color
        while q:
            cords = q.pop(0)
            for x, y in [[1, 0],[-1, 0],[0, 1],[0, -1]]:
                i, j = cords[0], cords[1]
                i += x
                j += y
                if 0 <= i < len(image) and 0 <= j < len(image[0]) and image[i][j] == init_color and (i, j) not in visited:
                    image[i][j] = color
                    visited.add((i, j))
                    q.append((i, j))

        return image