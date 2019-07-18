# -*- coding: utf-8 -*-
import heapq as pq
class MinimumSpanningTree(object):

    def findMinimumSpanningTree(self, graph, start_node, nodeNum):
        """
        :param graph: dict {src_node: [(dst_node1, cost1),(dst_node2, cost2),...]}
        :param start_node: string
        :return:
        """
        count = 1
        total_cost = 0 # to store minimum cost
        visited = set() # to track visited nodes
        visited.add('a')
        nextAvaiable = [] # to store next available nodes
        v = set() # to store vertex

        for node, cost in graph[start_node]:
            pq.heappush(nextAvaiable, (cost, node, (start_node, node)))

        while count < nodeNum:
            cost, node, vertex = pq.heappop(nextAvaiable)
            if node not in visited:
                for next_node, next_cost in graph[node]:
                    pq.heappush(nextAvaiable, (next_cost, next_node, (node, next_node)))
                visited.add(node)
                count += 1
                v.add(vertex)
                total_cost += cost

        return v, total_cost


graph = dict()
graph['a'] = [('b', 1),('d', 10),('e', 3)]
graph['b'] = [('a', 1),('d', 9),('c', 5)]
graph['c'] = [('b', 5),('d', 2),('f',4)]
graph['d'] = [('a',10),('b',9),('c',2),('e',7),('f',8)]
graph['e'] = [('a',3),('d',7),('f',6)]
graph['f'] = [('c',4),('d',8),('e',6)]

print MinimumSpanningTree().findMinimumSpanningTree(graph, 'a', 6)