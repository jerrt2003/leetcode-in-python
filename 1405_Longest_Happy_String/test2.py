import heapq


class Node:
    def __init__(self, char: str = None, count: int = None):
        self.char = char
        self.count = count

    def __lt__(self, other):
        return (
            self.count > other.count
        )  # change the direction of comparison for max heap


# create heap
heap = []

# create nodes
node1 = Node("a", 3)
node2 = Node("b", 1)
node3 = Node("c", 2)

heapq.heapify([node1, node2, node3])

# push nodes into heap
heapq.heappush(heap, node1)
heapq.heappush(heap, node2)
heapq.heappush(heap, node3)

# pop nodes from heap
print(heapq.heappop(heap).char)
print(heapq.heappop(heap).char)
heapq.heappush(heap, Node("d", 9))
print(heapq.heappop(heap).char)
print(heapq.heappop(heap).char)
