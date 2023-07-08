import collections
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        self.deadends = set(deadends)
        if "0000" in self.deadends:
            return -1
        self.visited_1 = collections.defaultdict(int)
        self.visited_2 = collections.defaultdict(int)
        q1, q2 = collections.deque(["0000"]), collections.deque([target])
        self.visited_1["0000"] = 0
        self.visited_2[target] = 0
        self.deadends = set(deadends)

        while q1 and q2:
            if len(q1) > len(q2):
                ret = self.update_q(q2, 1)
            else:
                ret = self.update_q(q1, 0)

            if ret != -1:
                return ret

        return -1

    def update_q(self, q: collections.deque, q_type: int) -> int:
        q_len = len(q)
        for _ in range(q_len):
            cur_combo = q.popleft()
            if (q_type == 0 and cur_combo in self.visited_2.keys()) or (
                q_type == 1 and cur_combo in self.visited_1.keys()
            ):
                return self.visited_1[cur_combo] + self.visited_2[cur_combo]

            for i in range(len(cur_combo)):
                digit = int(cur_combo[i])
                for click in [1, -1]:
                    next_digit = digit + click
                    if next_digit > 9:
                        next_digit = 0
                    elif next_digit < 0:
                        next_digit = 9
                    next_combo = cur_combo[:i] + str(next_digit) + cur_combo[i + 1 :]
                    if q_type == 0:
                        if (
                            next_combo not in self.visited_1.keys()
                            and next_combo not in self.deadends
                        ):
                            q.append(next_combo)
                            self.visited_1[next_combo] = self.visited_1[cur_combo] + 1
                    if q_type == 1:
                        if (
                            next_combo not in self.visited_2.keys()
                            and next_combo not in self.deadends
                        ):
                            q.append(next_combo)
                            self.visited_2[next_combo] = self.visited_2[cur_combo] + 1

        return -1
