import collections


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        custom_order = collections.defaultdict(int)
        for i, c in enumerate(order):
            custom_order[c] = i

        return "".join(sorted(s, key=lambda x: custom_order[x]))
