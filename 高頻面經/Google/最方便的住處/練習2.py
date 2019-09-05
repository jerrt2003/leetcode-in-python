# -*- coding: utf-8 -*-
import hash2, math

def best_apartment2(street, requirements):
    counter = hash2.Counter(requirements)
    remain = len(requirements)
    start = end = 0
    res, res_len = [], float('inf')
    while end < len(street):
        for poi in street[end]:
            if poi in counter:
                if counter[poi] > 0: remain -= 1
                counter[poi] -= 1
        end += 1
        while remain == 0:
            if end - start < res_len:
                res = []
                res_len = end - start
                mid = (start + end-1)/2.0
                if mid.is_integer(): res.append(int(mid))
                else: res.extend([math.floor(mid), math.ceil(mid)])
            elif end - start == res_len:
                mid = (start + end-1)/2.0
                if mid.is_integer(): res.append(int(mid))
                else: res.extend([math.floor(mid), math.ceil(mid)])
            for poi in street[start]:
                if poi in counter:
                    if counter[poi] >= 0: remain += 1
                    counter[poi] += 1
            start += 1
    return res

blocks = [['A'],['B','C'],['D','E','F'],['G'],['B','F'],['A','C','E'],['D'],['F','G'],['B','E']]
req = ['A','E','G']

assert best_apartment2(blocks, req) == [4, 6]