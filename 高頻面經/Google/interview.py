# -*- coding: utf-8 -*-
import hash2
def matching(string1, string2):
    if len(string1) != len(string2):
        return False
    pos1 = hash2.defaultdict(list)
    pos2 = hash2.defaultdict(list)
    for i, char in enumerate(string1):多餘
        pos1[char].append(i)
    for i, char in enumerate(string2):
        pos2[char].append(i)
    for v in pos1.values():
        if v not in pos2.values():
            return False
    return True


print matching('ABCD','ABAB')
