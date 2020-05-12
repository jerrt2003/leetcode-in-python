import collections


class Solution(object):
    def findJudge(self, N, trust):
        """
        T:O(E) S:O(n)
        Runtime: 684 ms, faster than 43.70% of Python online submissions for Find the Town Judge.
        Memory Usage: 17.8 MB, less than 33.33% of Python online submissions for Find the Town Judge.
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # if N == 1 and len(trust) == 0:
        #     return 1
        # trust1 = collections.defaultdict(int)
        # trust2 = collections.defaultdict(int)
        # for a, b in trust:
        #     trust1[b] += 1
        #     trust2[a] += 1
        # for k, v in trust1.iteritems():
        #     if v == N-1 and k not in trust2:
        #         return k
        # return -1

        # in_degree = [0]*(N+1)
        # out_degree = [0]*(N+1)
        # for a, b in trust:
        #     in_degree[b] += 1
        #     out_degree[a] += 1
        # for i in range(1, N+1):
        #     if in_degree[i] == N-1 and out_degree[i] == 0:
        #         return i
        # return -1

        degree = [0]*(N+1)
        for a, b in trust:
            degree[b] += 1
            degree[a] -= 1
        for i in range(1, N+1):
            if degree[i] == N-1:
                return i
        return -1



print Solution().findJudge(2, [[1,2]])