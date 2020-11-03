# -*- coding: utf-8 -*-
def findPath(input):
    pos_map = dict()
    x, y = 0, 0
    for i in range(ord('A'), ord('Z')+1):
        pos_map[chr(i)] = (x, y)
        y += 1
        if y == 5:
            x += 1
            y = 0

    res = ''
    prev_x, prev_y = 0, 0
    for char in input:
        char_x, char_y = pos_map[char]
        diff_x, diff_y = char_x - prev_x, char_y - prev_y
        if diff_x > 0:
            res += 'D'*abs(diff_x)
        elif diff_x < 0:
            res += 'U'*abs(diff_x)
        if diff_y > 0:
            res += 'R'*abs(diff_y)
        elif diff_y < 0:
            res += 'L'*abs(diff_y)
        res += '!'
        prev_x, prev_y = char_x, char_y
    return res


print findPath('CARS')