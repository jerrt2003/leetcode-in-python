from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # 我們將所有角色按照下列規則排序：
        # 1. 首先按照攻擊力降序排序(攻擊力大的排前面)
        # 2. 如果攻擊力相同，則按照防禦力升序排序(防禦力小的排前面)
        properties.sort(key=lambda x: (-x[0], x[1]))
        ans = 0
        max_def = -float("inf")

        for _, defence in properties:
            # 若防禦率小於目前最大防禦率，則該角色為弱角色
            # 因為其攻擊力必定小於前面某一角色的攻擊力: 因為我們攻擊力是降序排列的
            if defence < max_def:
                ans += 1
            else:
                max_def = defence

        return ans
