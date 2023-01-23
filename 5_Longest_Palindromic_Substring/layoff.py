class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        start, end, max_len = 0, 0, 0
        for i in range(len(s)):
            # l, r 需要從i-1,i+1開始不然接下來在步驟A/B時會重複計算cur_len的長度
            l, r = i-1, i+1
            cur_len = 1
            # 步驟A:由當前遍歷點向左延伸直到s[l]!=s[i] -> 即找出當前遍歷的左起始點
            while l >= 0 and s[l] == s[i]:
                cur_len += 1
                l -= 1
            # 步驟B:由當前遍歷點向右延伸直到s[r]!=s[i] -> 即找出當前遍歷的右起始點                
            while r < len(s) and s[r] == s[i]:
                cur_len += 1
                r += 1
            # 步驟C:左右起始點確定後開始繼續往左往右延伸直到不符合回文串條件即s[l]!=s[r]
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur_len += 2
                l -= 1
                r += 1
            # 步驟D:判斷當前回文串是否是最長 若是則update最長長度和左右邊界
            if cur_len > max_len:
                max_len = cur_len
                # 此處我們需要將邊界往回調1 因為之前步驟B/C時有+1才造成其迴圈條件不符合
                start, end = l+1, r-1
        return s[start:end+1]