# -*- coding: utf-8 -*-
class ThroneOrder(object):
    def __init__(self, root):
        self.head = Person(root)
        self.nameToNode = {root: self.head}

    def birth(self, parent, child):
        """
        Time Complexity: O(1)
        :param parent:
        :param child:
        :return:
        """
        if parent not in self.nameToNode:
            print('parent not exist')
        pNode = self.nameToNode[parent]
        cNode = Person(child)
        self.nameToNode[child] = cNode
        if pNode.lastChild is None:
            oldNext = pNode.next
            pNode.next = cNode
            cNode.next = oldNext
        else:
            oldNext = pNode.lastChild.next
            pNode.lastChild.next = cNode
            cNode.next = oldNext
        pNode.lastChild = cNode

    def dead(self, name):
        """
        Time Complexity: O(1)
        :param name:
        :return:
        """
        node = self.nameToNode[name]
        node.name = 'X'

    def getOrder(self):
        """
        Time Complexity: O(n)
        :return:
        """
        node = self.head
        order = []
        while node:
            if node.name != 'X':
                order.append(node.name)
                node = node.next
        return order



class Person(object):
    def __init__(self, name):
        self.name = name
        self.next = None
        self.lastChild = None