# -*- coding: utf-8 -*-
"""
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=491864&extra=page%3D2%26filter%3Dtypeid%26typeid%3D1019%26typeid%3D1019
"""

def pour(nums, K):
    count = 0
    W = K
    for i, num in enumerate(nums, 1):
        count += 1
        if W >= num:
            W -= num
        else:
            count += i*2
            W = K-num
    return count


print pour([1,2,3],3)