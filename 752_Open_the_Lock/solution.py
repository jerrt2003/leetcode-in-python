import collections
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"
        visited = set([start])
        deadends = set(deadends)
        if start not in deadends:
            queue = collections.deque([start])
        else:
            return -1
        ans = 0

        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                code = queue.popleft()
                if code == target:
                    return ans
                next_code_list = self.find_codes(code)
                for next_code in next_code_list:
                    if next_code not in deadends and next_code not in visited:
                        visited.add(next_code)
                        queue.append(next_code)
            ans += 1

        return -1

    def find_codes(self, code) -> List[str]:
        ret_list = []
        for i in range(len(code)):
            digit = code[i]
            for move in [1, -1]:
                next_digit = int(digit) + move
                if next_digit == 10:
                    next_digit = 0
                elif next_digit == -1:
                    next_digit = 9
                next_code = code[:i] + str(next_digit) + code[i + 1 :]
                ret_list.append(next_code)

        return ret_list
