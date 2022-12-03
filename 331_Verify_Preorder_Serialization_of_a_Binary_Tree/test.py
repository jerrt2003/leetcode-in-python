import unittest

from solution1 import Solution as S1
from solution2 import Solution as S2

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s1 = S1()
        self.s2 = S2()
        return super().setUp()

    def test1(self):
        preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
        self.assertTrue(self.s1.isValidSerialization(preorder))
        self.assertTrue(self.s2.isValidSerialization(preorder))

    def test2(self):
        preorder = "9,#,#,1"
        self.assertFalse(self.s1.isValidSerialization(preorder))
        self.assertFalse(self.s2.isValidSerialization(preorder))        


if __name__ == "__main__":
    unittest.main()