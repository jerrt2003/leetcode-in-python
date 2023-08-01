from typing import List


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        # 先找出所有需要加粗的位置並標記為 True
        mask = [False for _ in range(len(s))]
        for i in range(len(s)):
            prefix = s[i:]
            for word in words:
                if prefix.startswith(word):
                    for j in range(i, i + len(word)):
                        mask[j] = True

        ans = []
        # in_bold_str 用來標記當前下標 i 是否在加粗的字串中
        in_bold_str = False
        for i in range(len(s)):
            # 若當前下標 i 需要加粗，且當前下標 i 不在加粗的字串中，則加上 <b>，並將 in_bold_str 設為 True
            if mask[i] and not in_bold_str:
                ans.append("<b>")
                in_bold_str = True
            # 若當前下標 i 不需要加粗，且 in_bold_str 為 True, 表示找到加粗結束的位置，則加上 </b>，並將 in_bold_str 設為 False
            elif not mask[i] and in_bold_str:
                ans.append("</b>")
                in_bold_str = False
            # 記得將當前下標 i 的字元加入答案
            ans.append(s[i])
        # 若循環結束時 in_bold_str 為 True，表示在循環結束前最後一組字元需要加粗，加上 </b>
        if in_bold_str:
            ans.append("</b>")

        return "".join(ans)
