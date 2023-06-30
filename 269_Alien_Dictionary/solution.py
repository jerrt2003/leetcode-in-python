import collections
from typing import Dict, List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        char_indegree: Dict[str, int] = collections.defaultdict(int)
        char_adjacency_list: Dict[str, List[str]] = collections.defaultdict(list)

        for word in words:
            for w in word:
                if w not in char_indegree.keys():
                    char_indegree[w] = 0

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            idx = 0
            found = False
            while idx < min(len(word1), len(word2)):
                if word1[idx] != word2[idx]:
                    found = True
                    char_indegree[word2[idx]] += 1
                    char_adjacency_list[word1[idx]].append(word2[idx])
                    break
                idx += 1
            # 當input為[[a,b,c], [a, b]]時 <- non valid input
            if not found and len(word1) > len(word2):
                return ""

        ans = []
        q = []
        for k, v in char_indegree.items():
            if v == 0:
                q.append(k)
                ans.append(k)

        while q:
            cur_char = q.pop(0)
            for neighbor in char_adjacency_list[cur_char]:
                char_indegree[neighbor] -= 1
                if char_indegree[neighbor] == 0:
                    ans.append(neighbor)
                    q.append(neighbor)

        # 當最終任一char's indgress不為 0 時表示找不到valid topo sort
        return "" if any(v != 0 for v in char_indegree.values()) else "".join(ans)
