# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def __init__(self):
        self.logger = collections.OrderedDict()

    def logStart(self, id, start):
        self.logger[id] = False

    def logEnd(self, id, end):
        self.logger[id] = True

    def logPrint(self):
        for k, v in self.logger.iteritems():
            if v:
                print k


logger = Solution()
logger.logStart(1,1)
logger.logStart(2,2)
logger.logEnd(1,4)
logger.logStart(3,5)
logger.logEnd(3,6)
logger.logPrint()