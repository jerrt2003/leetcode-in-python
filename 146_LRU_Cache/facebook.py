class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.lru = LRU(capacity)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.lru.table:
            return -1
        node = self.lru.table[key]
        self.lru.removeNode(node)
        self.lru.addNode(node)
        return node.v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        new_node = Node(key, value)
        self.lru.addNode(new_node)


class Node(object):
    def __init__(self, k=None, v=None):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None


class LRU(object):
    def __init__(self, n):
        self.cap = n
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.table = dict()

    def addNode(self, node):
        if self.cap == 0:
            self.removeLastNode()
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head
        self.table[node.k] = node
        self.cap -= 1

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.cap += 1
        del self.table[node.k]
        return node

    def removeLastNode(self):
        node = self.tail.prev
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        del self.table[node.k]
        self.cap += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

obj = LRUCache(2)
obj.put(2,1)
obj.put(2,2)
obj.get(1)
obj.put(1,1)
obj.put(4,1)
obj.get(2)
