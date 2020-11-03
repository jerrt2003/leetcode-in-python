# -*- coding: utf-8 -*-
class LRUCache(object):

    def __init__(self, capacity):
        """
        T: O(1)
        S: O(1)
        Perf: Runtime: 224 ms, faster than 63.70% / Memory Usage: 22 MB, less than 37.78%
        :type capacity: int
        """
        self.cap = capacity
        self.lru = LRU()
        self.cache = dict()

    def get(self, key):
        """
        T: O(1)
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.lru.removeNode(node)
        self.lru.addNode(node)
        return node.v

    def put(self, key, value):
        """
        T: O(1)
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node = self.cache[key]
            node.v = value
            self.lru.removeNode(node)
            self.lru.addNode(node)
        else:
            if self.lru.size >= self.cap:
                node = self.lru.popLastNode()
                del self.cache[node.k]
            node = Node(key, value)
            self.cache[key] = node
            self.lru.addNode(node)

class LRU(object):
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.tail
        self.size = 0

    def addNode(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        self.size += 1

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def popLastNode(self):
        node = self.tail.prev
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.size -= 1
        return node

class Node(object):
    def __init__(self, k=None, v=None):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
obj.get(1)
obj.put(3,3)
obj.get(2)
obj.put(4,4)
obj.get(1)
obj.get(3)
obj.get(4)