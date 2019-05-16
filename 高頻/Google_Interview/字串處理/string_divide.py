# -*- coding: utf-8 -*-
class Solution(object):
    """
    From: https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=512114&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3086%5D%5Bvalue%5D%3D9%26searchoption%5B3086%5D%5Btype%5D%3Dradio%26searchoption%5B3089%5D%5Bvalue%5D%5B2%5D%3D2%26searchoption%5B3089%5D%5Btype%5D%3Dcheckbox%26searchoption%5B3046%5D%5Bvalue%5D%3D1%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26searchoption%5B3109%5D%5Bvalue%5D%3D2%26searchoption%5B3109%5D%5Btype%5D%3Dradio%26sortid%3D311%26orderby%3Ddateline
    """
    def divideString(self, input):

        def dfs(res, path, rest_of_candidate):
            if not rest_of_candidate:
                res.append(path)
            else:
                for char in rest_of_candidate[0].split(','):
                    dfs(res, path+char, rest_of_candidate[1:])

        split_res_1 = input.split('{')
        final_split = []
        for split_res in split_res_1:
            split_res = split_res.split('}')
            for _tmp in split_res:
                if _tmp != '':
                    final_split.append(_tmp)

        result = []
        dfs(result, '', final_split)

        return result

input = 'a{1,2,3}{b,c}d{8,9}'
print Solution().divideString(input)