import collections


class Solution(object):
    def canConvert(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        # graph = collections.defaultdict(list)
        # visit = collections.defaultdict(int)
        # for c1, c2 in zip(str1, str2):
        #     graph[c1].append(c2)
        #     visit.setdefault(c1, 0)
        #     visit.setdefault(c2, 0)
        #
        # def dfs(key):
        #     if visit[key] == 1:
        #         return True
        #     if visit[key] == -1:
        #         return False
        #     visit[key] = -1
        #     for nextChar in graph[key]:
        #         if not dfs(nextChar):
        #             return False
        #     visit[key] = 1
        #     return True
        #
        # for k in visit:
        #     if not dfs(k):
        #         return False
        # return True
        if str1 == str2: return True
        graph = dict()
        for c1, c2 in zip(str1, str2):
            if graph.setdefault(c1, c2) != c2:
                return False
        return len(set(str2)) < 26


# print Solution().canConvert('aabcc','ccdee')
# print Solution().canConvert('leetcode','codeleet')
print Solution().canConvert('ab','ba')