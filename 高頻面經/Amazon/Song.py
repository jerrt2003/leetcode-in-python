# -*- coding: utf-8 -*-
class Solution(object):
    def song(self, ride, song):
        new_song = sorted(song)
        m = len(song)
        pt1, pt2 = 0, m-1
        curr_max = -float('inf')
        res = None
        while pt1 < pt2:
            curr_len = new_song[pt1] + new_song[pt2]
            if curr_len <= ride-30 and curr_len > curr_max:
                curr_max = curr_len
                res = song.index(new_song[pt1]), song.index(new_song[pt2])
                pt1 += 1
            else:
                pt2 -= 1
        return res

#print Solution().song(110, [20,70,90,30,60,110])
print Solution().song(250, [100,180,40,120,10])