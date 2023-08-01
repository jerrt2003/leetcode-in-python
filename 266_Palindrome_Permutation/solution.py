import collections


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = collections.Counter(s)
        # 若 len(s) 為奇數 回文串中會有一個字符個數可為 1
        if len(s) % 2 == 1:
            flag = False
            for k, v in counter.items():
                # 當 k 字符為奇數時且 flag=False, 表示我們遇到可以置於中間的字符
                # 設 flag = True 然後繼續回圈 (ex. aaabb)
                if v % 2 == 1 and not flag:
                    flag = True
                    continue
                # 但當 flag 為 True時又遇到個數為奇數的字符 則我們無法在permuatation過後將 s 變成回文字符串
                elif v % 2 != 0:
                    return False
        else:
            for k, v in counter.items():
                if v % 2 != 0:
                    return False

        return True
