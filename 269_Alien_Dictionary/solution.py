import collections

from typing import List, Dict

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        ret = []
        # build indgree counter map and neighbor map
        indgree: Dict[str, int] = collections.defaultdict(int)
        neighbors: Dict[str, List[str]] = collections.defaultdict(list)
        self.buildGraph(words, indgree, neighbors)

        # check letter with indgree == 0 and push into queue
        q = []
        for k, v in indgree.items():
            if v == 0:
                q.append(k)

        # BFS: when a letter is visited, put into ret
        # and reduce all it's neighbor's indgree count by 1
        # only when a neighbor's indgree == 0 push into queue
        while q:
            node = q.pop(0)
            ret.append(node)
            for neighbor in neighbors[node]:
                indgree[neighbor] -= 1
                if indgree[neighbor] == 0:
                    q.append(neighbor)
        
        return ''.join(ret) if len(ret) == len(indgree.keys()) else ""


    def buildGraph(self, words: List[str], indgree: Dict[str, int], neighbors: Dict[str, List[str]]) -> None:
        
        def init_indegree(word):
            for w in word:
                if w not in indgree.keys():
                    indgree[w] = 0

        for idx in range(len(words)-1):
            word1 = words[idx]
            word2 = words[idx+1]
            init_indegree(word1)
            init_indegree(word2)
            for w1, w2 in zip(word1, word2):                                    
                if w1 != w2:
                    indgree[w2] += 1
                    neighbors[w1].append(w2)
                    break

            

            