import collections


class Solution(object):
    def alienOrder(self, words):
        """
        Facebook
        Topo Sort
        T:O(V+E) S:O(V+E)
        Runtime: 20 ms, faster than 85.75% of Python online submissions for Alien Dictionary.
        Memory Usage: 12.8 MB, less than 68.31% of Python online submissions for Alien Dictionary.
        :type words: List[str]
        :rtype: str
        """
        self.visit = {c : 0 for word in words for c in word}
        self.graph = collections.defaultdict(set)
        for i in range(len(words)-1):
            orderFound = False
            w1, w2 = words[i], words[i+1]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    orderFound = True
                    self.graph[w1[j]].add(w2[j])
                    break
            if not orderFound and len(w1) > len(w2):
                return ""
        self.ans = []
        for k in self.visit:
            if self.visit[k] == 0:
                if not self.dfs(k):
                    return ""
        self.ans.reverse()
        return ''.join(self.ans)

    def dfs(self, k):
        if self.visit[k] == -1:
            return False
        if self.visit[k] == 1:
            return True
        self.visit[k] = -1
        for nei in self.graph[k]:
            if not self.dfs(nei):
                return False
        self.ans.append(k)
        self.visit[k] = 1
        return True

print Solution().alienOrder(["wrt","wrf","er","ett","rftt"])
print Solution().alienOrder(["z","z"])
print Solution().alienOrder(["abc","ab"])
print Solution().alienOrder(["wrt","wrtkj"])
