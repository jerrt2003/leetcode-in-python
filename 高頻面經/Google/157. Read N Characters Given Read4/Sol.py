# -*- coding: utf-8 -*-
"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution(object):
    def read(self, buf, n):
        """
        Time: O(n)
        Space: O(n)
        Perf: Runtime: 16 ms, faster than 96.93% / Memory Usage: 11.7 MB, less than 87.05%
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        count = 0
        while True:
            _buf = ['']*4
            _res = read4(_buf)
            idx = min(_res, n-count)
            for i in range(idx):
                buf[count] = _buf[i]
                count += 1
            if _res < 4 or count == n:
                return count