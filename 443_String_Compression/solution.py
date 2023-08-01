from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        # pointer i: current idx
        # pointer j: the last char idx
        j = 0
        count = 0
        for i in range(len(chars)):
            if chars[i] != chars[j]:
                j += 1
                if count != 1:
                    for chr in str(count):
                        chars[j] = chr
                        j += 1
                count = 1
            else:
                count += 1
        j += 1
        if count != 1:
            for chr in str(count):
                chars[j] = chr
                j += 1
        return j
