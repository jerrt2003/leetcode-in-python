class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # solution 2: 總indegree == 總outdegree
        # 一個正常node會提供 1 個indegree + 2 個outdgree (indgree 相當於消耗掛載點(for子節點), outdegree 為提供掛載點)
        # 一個 ‘None' node會提供 1 個indegree
        # 在遍歷樹時任何時間 indegree <= outdegree (消耗掛載應永遠小於提供掛載)
        # 只要indegree > outdegree 即為非法
        # diff == outdegree - indegree
        diff: int = 1
        preorder = preorder.split(",")
        for node in preorder:
            diff -= 1
            if diff < 0:
                return False            
            if node != "#":
                diff += 2
        return diff == 0