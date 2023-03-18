from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans: List[str] = []
        self.dfs(num, 0, 0, "", target, ans)
        return ans
    


    def dfs(self, num: str, start:int, eval: int, path: str, target: int, ans: List[str]):
        if start == len(num):
            if eval == target:
                ans.append(path)
                return
        for i in range(start, len(num)):
            # we can have num '0' but not '01' '02'
            # if <num> start with 0 we should break
            if num[start] == 0 and i > start+1:
                break
            if start == 0:
                self.dfs(num, i+1, int(num[start:i+1]), num[start:i+1], target, ans)
            self.dfs(num, i+1, eval + int(num[start:i+1]), path + "+" + num[start:i+1], target, ans)
            self.dfs(num, i+1, eval - int(num[start:i+1]), path + "-" + num[start:i+1], target, ans)


if __name__ == "__main__":
    Solution().addOperators('123',6)