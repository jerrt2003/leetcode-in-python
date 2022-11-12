class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        T:O(mn) S:O(1)
        Runtime: 16 ms, faster than 91.30% of Python online submissions for Camelcase Matching.
        Memory Usage: 12.7 MB, less than 57.78% of Python online submissions for Camelcase Matching.
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        ans = []
        for query in queries:
            ans.append(self.check(query, pattern))
        return ans


    def check(self, query, pattern):
        i = j = 0
        while i < len(query) and j < len(pattern):
            if query[i] == pattern[j]:
                i += 1
                j += 1
            elif query[i] != pattern[j] and ord(query[i]) > 90:
                i += 1
            else:
                return False
        if j < len(pattern):
            return False
        while i < len(query):
            if ord(query[i]) < 90:
                return False
            i += 1
        return True





print Solution().camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB")
print Solution().camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBa")
print Solution().camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBaT")