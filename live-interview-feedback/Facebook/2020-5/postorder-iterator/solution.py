class Solution(object):
    def __init__(self, node):
        self.stack = []
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self):
        """
        check if there is a next
        :return: bool
        """
        return len(self.stack) > 0

    def getNext(self):
        curr = self.stack.pop()
        if self.stack and self.stack[-1].right:
            node = self.stack[-1].right
            while node:
                self.stack.append(node)
                node = node.left
        return curr.val


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


if __name__ == '__main__':
    root = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    root.left = node2
    root.right = node3
    node2.left = node4
    node2.right = node5
    node5.left = node6

    obj = Solution(root)
    while obj.hasNext():
        print obj.getNext()