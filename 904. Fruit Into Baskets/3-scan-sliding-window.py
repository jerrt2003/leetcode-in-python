import collections


class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if not tree: return 0
        bucket = collections.defaultdict(int)
        pt1, pt2 = 0, 1
        bucket[tree[pt1]] += 1
        ret = 1
        while pt2 < len(tree):
            bucket[tree[pt2]] += 1
            while len(bucket) > 2:
                bucket[tree[pt1]] -= 1
                if bucket[tree[pt1]] == 0:
                    del bucket[tree[pt1]]
                pt1 += 1
            ret = max(ret, pt2-pt1+1)
            pt2 += 1
        return ret


print Solution().totalFruit([1,2,1])