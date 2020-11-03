# -*- coding: utf-8 -*-
# http://tinyurl.com/y4ebtbbp
# 2019(4-6)
class Solution(object):
    def findDuplicate(self, l1, l2):
        """
        用two pointer方法实现两数组找交集的函数，复用两次即可
        Time: O(n)
        Space: O(n)
        :param l1:
        :param l2:
        :return:
        """
        pt1, pt2, res = 0, 0, []
        while pt1 < len(l1) and pt2 < len(l2):
            if l1[pt1] == l2[pt2]:
                res.append(l1[pt1])
                pt1+=1
                pt2+=1
            elif l1[pt1] > l2[pt2]:
                pt2+=1
            else:
                pt1+=1
        return res

assert Solution().findDuplicate([1,2,3],[2,3,4]) == [2,3]
assert Solution().findDuplicate([],[1,2]) == []
assert Solution().findDuplicate([1,2],[3,4]) == []
