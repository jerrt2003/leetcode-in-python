import unittest
from solution2 import Solution


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        node0 = TreeNode(0)
        node1 = TreeNode(1)
        node1_2 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)

        node1.left = node0
        node1.right = node3

        node2.left = node1_2
        node2.right = node4

        self.assertEqual([0, 1, 1, 2, 3, 4], self.s.getAllElements(node1, node2))


if __name__ == "__main__":
    unittest.main()
