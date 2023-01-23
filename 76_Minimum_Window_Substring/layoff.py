import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # t_counter: 紀錄t中字母出現的頻率
        t_counter = collections.Counter(t)
        # c_counter: 紀錄當前window字母出現在頻率 
        c_counter = collections.defaultdict(int)
        # form: 紀錄當前window是否已經符合條件(i.e. window包含所有在t中的字母)
        form = 0
        # 開始遍歷s
        l, r = 0, 0
        ans = ""
        min_len = float('inf')
        while r < len(s):
            # s[r]:當前遍歷的字符
            # 若當前遍歷的字符出現在t中時更新c_counter
            if s[r] in t_counter.keys():
                c_counter[s[r]] += 1
                # 當c_counter[字符] == t_counter[字符]時表示當前window已經有足夠的[字符]數目
                # 所以form+=1
                if c_counter[s[r]] == t_counter[s[r]]:
                    form += 1
            # 當form == len(t_counter)表示當前window已經包含t的所有字符
            # 開始嘗試縮小window
            while form == len(t_counter) and l <= r:
                # 若當前window小於min_len 我們就update min_len以及ans
                if (r-l+1) < min_len:
                    min_len = (r-l+1)
                    ans = s[l:r+1]
                # l開始右移 右移過程中遇到s[l]中現在t中時要update c_counter, 
                # 而當c_counter[字符] < t_counter[字符]時表示當前window不符合條件:form -= 1,停止移動l
                if s[l] in t_counter.keys():
                    c_counter[s[l]] -= 1
                    if c_counter[s[l]] < t_counter[s[l]]:
                        form -= 1
                l += 1
            r += 1
        return ans