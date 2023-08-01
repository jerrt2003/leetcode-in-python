import unittest

from solution import Codec


class Test(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test1(self):
        codec = Codec()
        self.assertEqual(
            codec.decode(codec.encode(["hello", "world"])), ["hello", "world"]
        )

    def test2(self):
        codec = Codec()
        self.assertEqual(
            codec.decode(codec.encode(["`Ejy7", "mjax", "Z vcCvs"])),
            ["`Ejy7", "mjax", "Z vcCvs"],
        )


if __name__ == "__main__":
    unittest.main()
