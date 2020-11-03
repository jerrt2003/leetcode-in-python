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
        if key not in self.lru.ref:
            return -1
        node = self.lru.ref[key]
        self.lru.remove(node)
        self.lru.add(node)
        return node.v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.lru.ref:
            node = self.lru.ref[key]
            node.v = value
            self.lru.remove(node)
        else:
            node = Node(key, value)
            self.lru.ref[key] = node
        self.lru.add(node)

class LRU(object):
    def __init__(self, n):
        self.cap = n
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head
        self.ref = dict()

    def add(self, node):
        if self.cap == 0:
            self.removeLast()
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head
        self.cap -= 1

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.cap += 1

    def removeLast(self):
        last = self.tail.prev
        self.tail.prev = last.prev
        last.prev.next = self.tail
        self.cap += 1
        del self.ref[last.k]

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