import collections


class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        2 layer of topo sort: item sort then group sort
        T: O(V+E) S:O(V+E)
        Runtime: 428 ms, faster than 78.16% of Python online submissions for Sort Items by Groups Respecting Dependencies.
        Memory Usage: 29.1 MB, less than 100.00% of Python online submissions for Sort Items by Groups Respecting Dependencies.
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """
        self.group_item_map = collections.defaultdict(list) # key: group-id value: item
        self.graph_group = collections.defaultdict(list)
        self.graph_item = collections.defaultdict(list)

        for k, v in enumerate(group):
            if v == -1:
                self.group_item_map[m].append(k)
                group[k] = m
                m += 1
            else:
                self.group_item_map[v].append(k)

        for after, beforeItem in enumerate(beforeItems):
            for b in beforeItem:
                if group[after] == group[b]:
                    self.graph_item[after].append(b)
                else:
                    self.graph_group[group[after]].append(group[b])

        for groupId, itemList in self.group_item_map.iteritems():
            sortOrder = []
            visit = dict()
            for item in itemList:
                visit[item] = 0
            for item in itemList:
                if not self.dfs(item, sortOrder, visit):
                    return []
            self.group_item_map[groupId] = sortOrder

        groupIds = self.group_item_map.keys()
        groupIdsSortOrder = []
        visit = dict()
        for groupId in groupIds:
            visit[groupId] = 0
        for groupId in groupIds:
            if not self.dfs(groupId, groupIdsSortOrder, visit, isGroup=True):
                return []

        ret = []
        for id in groupIdsSortOrder:
            ret += self.group_item_map[id]

        return ret

    def dfs(self, i, ans, visit, isGroup=False):
        if visit[i] == 1:
            return True
        if visit[i] == -1:
            return False
        visit[i] = -1
        if not isGroup:
            for nextI in self.graph_item[i]:
                if not self.dfs(nextI, ans, visit):
                    return False
        else:
            for nextI in self.graph_group[i]:
                if not self.dfs(nextI, ans, visit, isGroup=True):
                    return False
        visit[i] = 1
        ans.append(i)
        return True

# print Solution().sortItems(8,2,[-1,-1,1,0,0,1,0,-1],[[],[6],[5],[6],[3],[],[4],[]])
print Solution().sortItems(8,2,[-1,-1,1,0,0,1,0,-1],[[],[6],[5],[6],[3,6],[],[],[]])
# print Solution().sortItems(5,5,[2,0,-1,3,0],[[2,1,3],[2,4],[],[],[]])