from typing import List


class Solution:
    # 這個程式碼首先把新區間newInterval的開始和結束時間儲存到s和e。
    # 程式碼創建了一個空列表ans來存放最終的結果。
    # 然後，程式碼進入一個while循環，循環遍歷intervals裡的每個區間：
    # 如果新區間的開始時間s小於或等於當前區間的結束時間curr_e，那麼可能存在重疊區間需要合併。這時，程式碼會檢查新區間的結束時間e是否小於當前區間的開始時間curr_s，如果是的話，那麼就可以提前結束循環，因為新區間已經找到了插入的位置，且新區間與後續的區間不會有重疊。
    # 如果新區間的開始時間s大於當前區間的結束時間curr_e，那麼就沒有重疊區間需要合併，程式碼會將當前區間加入到結果列表ans中。
    # 在循環結束後，程式碼將更新後的新區間（可能已經與一個或多個區間合併過）加入到結果列表ans中。
    # 然後，程式碼將intervals列表中剩餘的區間（這些區間與新區間不會有重疊）加入到結果列表ans中。
    # 最後，程式碼返回結果列表ans，這就是插入新區間並合併可能的重疊區間後的結果。

    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        s, e = newInterval[0], newInterval[1]
        i = 0
        ans = []
        while i < len(intervals):
            curr_s, curr_e = intervals[i][0], intervals[i][1]
            if s <= curr_e:
                if e < curr_s:
                    break
                s = min(s, curr_s)
                e = max(e, curr_e)
            else:
                ans.append(intervals[i])
            i += 1
        ans.append([s, e])
        ans += intervals[i:]
        return ans
