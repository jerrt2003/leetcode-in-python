from typing import Dict

class LRUNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = LRUNode()
        self.tail = self.head
        self.hash: Dict[int, LRUNode] = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if not key in self.hash.keys():
            return False
        node = self.hash[key]
        # remove node from current pos
        self.remove_node(node)
        # move node to the last of the linkedlist
        self.insert_node(node)
        return True

    def put(self, key: int, value: int) -> None:
        if key in self.hash.keys():
            node = self.hash[key]
            node.val = value
            self.remove_node(node)
            self.insert_node(node)
        else:
            while self.capacity == 0:
                self.remove_node(self.head.next)
                self.capacity += 1
            new_node = LRUNode(key=key, value=value)
            self.insert_node(new_node)

    def remove_node(self, node: LRUNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        del(self.hash[node.key])
        
    def insert_node(self, node: LRUNode) -> None:
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node
        self.hash[node.key] = node       


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)