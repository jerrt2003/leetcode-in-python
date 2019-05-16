# -*- coding: utf-8 -*-
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class GoogleInterview(object):
    def Solution(self, root):

        def delete(node, count, prev_node, visited):
            if node in visited:
                return
            visited.append(node)
            if count % 2 == 1:
                delete(node.next, count+1, node, visited)
            else:
                prev_node.next = node.next
                delete(node.next, count+1, prev_node, visited)

        delete(root, 1, None, [])

        visited = []
        while root not in visited:
            print root.val
            visited.append(root)
            root = root.next

node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
node_5.next = node_1

GoogleInterview().Solution(node_1)