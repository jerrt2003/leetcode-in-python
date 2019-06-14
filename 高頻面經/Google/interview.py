# -*- coding: utf-8 -*-
import collections
def matching(string1, string2):
    if len(string1) != len(string2):
        return False
    pos1 = collections.defaultdict(list)
    pos2 = collections.defaultdict(list)
    for i, char in enumerate(string1):
        pos1[char].append(i)
    for i, char in enumerate(string2):
        pos2[char].append(i)
    for v in pos1.values():
        if v not in pos2.values():
            return False
    return True


print matching('ABCD','ABAB')
