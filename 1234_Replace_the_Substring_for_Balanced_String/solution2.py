from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        counter = Counter(s)
        m = len(s)//4
        if all(counter[x] == m for x in "QWER"):
            return 0
        j, ans = 0, float('inf')
        for i, c in enumerate(s):
            counter[c] -= 1 
            while j <= i and all(counter[x] <= m for x in "QWER"):
                ans = min(ans, i-j+1)
                counter[s[j]] += 1
                j+=1
        return ans