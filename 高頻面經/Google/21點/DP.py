# -*- coding: utf-8 -*-
"""
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=497125&extra=page%3D2%26filter%3Dtypeid%26typeid%3D1019%26typeid%3D1019
https://www.1point3acres.com/bbs/thread-311254-1-1.html
"""

class Solution(object):
    def bustProbability(self):
        DP = [0]
        for i in range(1, 22):
            if i > 10: