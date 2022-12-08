from typing import Dict, List

class Solution:
    def romanToInt(self, s: str) -> int:
        char_num_maps: Dict[str, int] = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        char_list: List[str] = [w for w in s]
        ans: int = 0
        while char_list:
            char = char_list.pop()
            ans += char_num_maps[char]
            if char_list and char_num_maps[char_list[-1]] < char_num_maps[char]:
                char = char_list.pop()
                ans -= char_num_maps[char]
        return ans
