class Soltuion(object):
    def get_all_combination(self, input):
        # Facebook
        # T:O(V) S:O(V)
        ans = []
        def dfs(idx, path):
            if idx == len(input) and sum(path) == 100:
                ans.append(path)
                return
            for i in range(idx+1, len(input)+1):
                dfs(i, path + [int(input[idx:i])])
                dfs(i, path + [-1 * int(input[idx:i])])

        dfs(0, [])
        return ans

print Soltuion().get_all_combination("123456789")





