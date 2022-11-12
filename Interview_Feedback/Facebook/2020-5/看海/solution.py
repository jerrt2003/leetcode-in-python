class Solution(object):
    def findBuilding(self, buildings):
        ans = []
        for b in buildings:
            if not ans or b > ans[-1]:
                ans.append(b)

        return len(ans)

print Solution().findBuilding([7, 4, 8, 2, 9])