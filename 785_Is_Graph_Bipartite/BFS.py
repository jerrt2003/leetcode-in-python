# BFS
class Solution(object):
    def isBipartite(self, graph):
        """
        Solution: BFS
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: https://leetcode.com/problems/is-graph-bipartite/discuss/115503/java-BFS
        TP:
        - Basic idea is that we want to divide all nodes into 2 groups, let's say black and white
        - Follow inline comment
        :type graph: List[List[int]]
        :rtype: bool
        """
        visited = [
            0 for _ in range(len(graph))
        ]  # we'll use 3 numbers to represent 3 status: (0, not visited), (1, white), (-1, black)
        for i in range(len(graph)):
            if (
                graph[i] and visited[i] == 0
            ):  # Only check when node has edges (neighbors) and not visit yet
                visited[
                    i
                ] = 1  # If a node is not visit, we'll mark it as white, WHY? because if this node can't be white, then it must be marked already
                q = [i]  # Start BFS
                while q:
                    curr = q.pop(0)
                    for j in graph[curr]:
                        if visited[j] == 0:
                            visited[j] = 1 if visited[curr] == -1 else 1
                            q.append(j)
                        elif visited[j] == visited[curr]:
                            return False
        return True
