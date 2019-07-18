class Solution(object):
    def findAllCombination(self, s):
        m = len(s)

        def dfs(i):
            ret = []
            cacheList = []
            cache = ''
            while i < m:
                if s[i] == '}':
                    if cache and cacheList:
                        cacheList = [a+cache for a in cacheList]
                        ret.extend(cacheList)
                    elif cacheList:
                        ret.extend(cacheList)
                    elif cache:
                        ret.append(cache)
                    return i, ret
                elif s[i] == '{':
                    i, insideResult = dfs(i+1)
                    if cache:
                        cacheList = [cache + a for a in insideResult]
                        cache = ''
                elif s[i] == ',':
                    if cache and cacheList:
                        cacheList = [a + cache for a in cacheList]
                        ret.extend(cacheList)
                    elif cache:
                        ret.append(cache)
                    cacheList = []
                    cache = ''
                elif s[i].isalnum():
                    cache += s[i]
                i += 1
            if cache and cacheList:
                ret = [a + cache for a in cacheList]
            elif cache:
                ret.append(cache)
            return i, ret

        _, result = dfs(0)
        return result


#assert Solution().findAllCombination('a{b,c{1,2}d,e}f') == ['abf','ac1df','ac2df','aef']
assert Solution().findAllCombination('a{b,c{1,2}}{h,i}') == ['abh','abi','ac1h','ac1i','ac2h','ac2i']