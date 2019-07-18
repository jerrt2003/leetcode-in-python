# -*- coding: utf-8 -*-
class Solution(object):
    def __init__(self):
        self.nodes = dict()
        node = Node()
        self.head = node
        self.end = node

    def logStart(self, id, start):
        """
        T:O(1)
        :param id:
        :param start:
        :return:
        """
        node = Node(id=id, start=start)
        self.nodes[id] = node
        self.end.next = node
        self.end = self.end.next

    def logEnd(self, id, end):
        """
        T:O(1)
        :param id:
        :param end:
        :return:
        """
        self.nodes[id].end = end

    def logPrint(self):
        """
        T:O(n)
        :return:
        """
        node = self.head
        while node.next:
            node = node.next
            if self.nodes[node.id].end != None:
                print node.id

class Node(object):
    def __init__(self, id=None, start=None):
        self.id = id
        self.start = start
        self.end = None
        self.next = None


logger = Solution()
logger.logStart(1,1)
logger.logStart(2,2)
logger.logEnd(1,4)
logger.logStart(3,5)
logger.logEnd(3,6)
logger.logEnd(2,7)
logger.logPrint()