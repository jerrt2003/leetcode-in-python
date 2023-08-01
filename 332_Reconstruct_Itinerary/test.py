import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        ans = ["JFK", "MUC", "LHR", "SFO", "SJC"]
        self.assertEqual(ans, self.s.findItinerary(tickets))

    def test2(self):
        tickets = [
            ["JFK", "SFO"],
            ["JFK", "ATL"],
            ["SFO", "ATL"],
            ["ATL", "JFK"],
            ["ATL", "SFO"],
        ]
        ans = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
        self.assertEqual(ans, self.s.findItinerary(tickets))

    def test3(self):
        tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
        ans = ["JFK", "NRT", "JFK", "KUL"]
        self.assertEqual(ans, self.s.findItinerary(tickets))


if __name__ == "__main__":
    unittest.main()
