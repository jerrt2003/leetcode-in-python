import collections


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        visited = [0 for _ in range(n)]
        outdegree = [0 for _ in range(n)]
        node_neighbors = collections.defaultdict(list)

        for s, e in edges:
            outdegree[s] += 1
            outdegree[e] += 1
            node_neighbors[s].append(e)
            node_neighbors[e].append(s)

        q = collections.deque([])
        for i, v in enumerate(outdegree):
            if v == 1:
                q.append(i)
                visited[i] = 1

        ans = []
        while q:
            tmp_ans = []
            for _ in range(len(q)):
                node = q.popleft()
                tmp_ans.append(node)
                for neighbor in node_neighbors[node]:
                    outdegree[neighbor] -= 1
                    if visited[neighbor] == 0 and outdegree[neighbor] == 1:
                        visited[neighbor] = 1
                        q.append(neighbor)
            ans = tmp_ans

        return ans
