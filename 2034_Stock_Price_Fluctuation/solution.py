# Doubly LinkedList
# TLE
import collections


class Node:
    def __init__(self, price, prev, next):
        self.price = price
        self.prev = prev
        self.next = next


class StockPrice:
    def __init__(self):
        self.head = Node(float("inf"), None, None)
        self.tail = Node(-float("inf"), None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.tsToNodeMap = collections.defaultdict(Node)
        self.key = -float("inf")

    def update(self, timestamp: int, price: int) -> None:
        self.key = max(self.key, timestamp)
        if not timestamp in self.tsToNodeMap.keys():
            node = Node(price, None, None)
            head = self.head
            while head.next != self.tail:
                if price < head.price and price >= head.next.price:
                    break
                head = head.next
            node.next = head.next
            node.next.prev = node
            node.prev = head
            head.next = node

            self.tsToNodeMap[timestamp] = node
        else:
            node = self.tsToNodeMap[timestamp]
            node.prev.next = node.next
            node.next.prev = node.prev

            node.price = price
            head = self.head
            while head.next != self.tail:
                if price < head.price and price >= head.next.price:
                    break
                head = head.next
            node.next = head.next
            node.next.prev = node
            node.prev = head
            head.next = node

    def current(self) -> int:
        return self.tsToNodeMap[self.key].price

    def maximum(self) -> int:
        return self.head.next.price

    def minimum(self) -> int:
        return self.tail.prev.price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
