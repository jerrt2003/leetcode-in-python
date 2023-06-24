class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = len(s)
        # 在 Python 中，"list * n" 操作會創建 n 個列表的淺拷貝，而不是獨立的列表。一個列表的淺拷貝是一個新列表，包含對原始列表所持有的元素的引用。所以，當你改變一個元素時，所有的列表都會被更新。
        # 而 "列表推導式" 的方法 ([[False] * m for _ in range(m)]) 會創建獨立的列表。
        DP = [[False] * m for _ in range(m)]
        for i in range(m):
            DP[i][i] = True

        max_len = -float("inf")
        start, end = 0, 0
        for j in range(1, len(s)):
            for i in range(0, j):
                # ChatGPT
                # 對於 j - i < 2 的判斷，確實會在一些例子（如 "cbbd"）中導致程式失敗。
                # 我之前的解釋忽略了這種情況。在這種情況下，我們應該檢查整個子串是否為回文，而不僅僅是兩個字符。所以這裡 j - i < 2 的條件不正確，
                # 應該是 j - i + 1 <= 2。
                if s[i] == s[j] and (DP[i + 1][j - 1] or j - i + 1 <= 2):
                    DP[i][j] = True
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        start, end = i, j

        return s[start : end + 1]
