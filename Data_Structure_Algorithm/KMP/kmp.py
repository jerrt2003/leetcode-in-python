class KMP:
    def match(self, s, p):
        n, m = len(s), len(p)
        nxt = self.build(p)
        ans = []
        j = 0
        for i in range(n):
            while j > 0 and s[i] != s[j]:
                j = nxt[j]
            if s[i] == p[j]:
                j += 1
            if j == m:
                ans.append(i-m+1)
                j = nxt[j]
        return ans

    def build(self, p):
        m = len(p)
        nxt = [0, 0]
        j = 0
        for i in range(1, m):
            while j > 0 and p[i] != p[j]:
                j = nxt[j]
            if p[i] == p[j]:
                j += 1
            nxt.append(j)
        return nxt

print KMP().match("abcab","ab")