from typing import List, Dict

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.num_char_maps: Dict[str, str] = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }
        self.ret: List[str] = []
        if digits:
            path = ""
            self.helper(0, path, digits)
        return self.ret


    def helper(self, k: int, path: str, digits: str) -> None:
        if k == len(digits):
            self.ret.append(path)
            return
        for c in self.num_char_maps[digits[k]]:
            self.helper(k+1, path + c, digits)
