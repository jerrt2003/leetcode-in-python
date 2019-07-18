# -*- coding: utf-8 -*-
class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        Solution: DFS + post_order_traversal + pre_order_traversal
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: https://leetcode.com/problems/sum-of-distances-in-tree/solution/
        TP:
        - What is the distance value a node to all of other node?
            - To find ans[curr_node], say we already know following 2 information:
                - ans[child_node]: to present the distance of this child_node to all its decedents.
                - count[child_node]: to present total node count for this subtree (e.g. this child node + all its decedents nodes count)
                - The we'll have ans[curr_node] = ans[child_node] + count[child_node] (since distance between each node in this subtree will increase by 1 (distance between curr_node and child_node)
            - The above steps represent a post order traversal (left-right-root)
                - do the leaf node first so its information will be available to root node
        - After we collect ans, count information from previous search using post-order-traversal, we can now compute the distance for each node to all other nodes
            - actually at this moment only the "root" node will have ans, but that's ok, we can derive other nodes 'ans' from it by:
                - ans[child] = ans[curr_node] - count[child] + (N - count[child])
                - Why minus count[child]: since we want to know ans[child] and we need to subtract all distance of child subtree
                - Why plus (N - count[child]): since the other side of tree to this child node will add 1 distance
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # To build the tree using dict/set
        import collections
        graph = collections.defaultdict(set)
        for k, v in edges:
            graph[k].add(v)
            graph[v].add(k)
        count = [1]*N
        ans = [0]*N

        def dfs(curr_node, parent):
            for child in graph[curr_node]:
                if child != parent:
                    # post order traversal
                    dfs(child, curr_node) # do the leaf node first
                    count[curr_node] += count[child] # then come back to calculate curr node
                    ans[curr_node] += ans[child] + count[child]

        def dfs2(curr_node, parent):
            for child in graph[curr_node]:
                if child != parent:
                    ans[child] = ans[curr_node] - count[child] + (N - count[child])
                    dfs2(child, curr_node)

        dfs(0, None)
        dfs2(0, None)
        return ans

#N = 6
#edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]

N = 1
edges = []

sol = Solution()
print sol.sumOfDistancesInTree(N, edges)