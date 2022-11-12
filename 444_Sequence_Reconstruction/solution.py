import collections


class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        N = len(org)
        in_degree = [0 for _ in range(N+1)]
        out_edge = collections.defaultdict(list)
        if not seqs or all(not seq for seq in seqs):
            return False
        for seq in seqs:
            for i in range(len(seq)-1):
                s, e = seq[i], seq[i+1]
                if s not in out_edge or e not in out_edge[s]:
                    in_degree[e] += 1
                    out_edge[s].append(e)
        q = collections.deque([])
        for i in range(1, N+1):
            if in_degree[i] == 0:
                q.append(i)
        ans = []
        while q:
            l = len(q)
            if l > 1:
                return False
            curr = q.popleft()
            ans.append(curr)
            for nei in out_edge[curr]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        return ans == org


# print Solution().sequenceReconstruction([4,1,5,2,6,3], [[5,2,6,3],[4,1,5,2]])
# print Solution().sequenceReconstruction([1,2,3], [[1,2],[1,3]])
# print Solution().sequenceReconstruction([1,2,3], [[1,2],[1,3],[2,3]])
# print Solution().sequenceReconstruction([1],[])
# print Solution().sequenceReconstruction([1],[[1],[1],[1]])
print Solution().sequenceReconstruction([1],[[2]])