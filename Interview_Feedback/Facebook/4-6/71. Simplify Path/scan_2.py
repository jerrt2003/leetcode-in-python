# -*- coding: utf-8 -*-
class Solution(object):
    def simplifyPath(self, path):
        """
        Time: O(n)
        Perf: Runtime: 24 ms, faster than 80.80% / Memory Usage: 11.8 MB, less than 50.00%
        :type path: str
        :rtype: str
        """
        stack = []
        cache = ''
        for i in range(len(path)):
            if path[i] == '/':
                if not cache:
                    continue
                elif cache == '..':
                    if stack:
                        stack.pop()
                    cache = ''
                elif cache == '.':
                    cache = ''
                    continue
                else:
                    stack.append(cache)
                    cache = ''
            else:
                cache += path[i]
        if cache:
            if cache == '..':
                if stack:
                    stack.pop()
            elif cache == '.':
                return '/' + '/'.join(stack)
            else:
                stack.append(cache)
        return '/'+'/'.join(stack)

#assert Solution().simplifyPath('/home/') == '/home'
#assert Solution().simplifyPath('/../') == '/'
#assert Solution().simplifyPath('/home//foo/') == '/home/foo'
#assert Solution().simplifyPath('/a/./b/../../c/') == '/c'
#assert Solution().simplifyPath('/a/../../b/../c//.//') == '/c'
#assert Solution().simplifyPath('/a//b////c/d//././/..') == '/a/b/c'
assert Solution().simplifyPath('/..') == '/'