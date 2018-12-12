# -*- coding: utf-8 -*-
class Codec:
    def __init__(self):
        """
        Solution: Using Hash and Dict
        Time Complexity: O(1)
        Space Complexity:
        Thinking process:
        - Take the Long URL and hash it
        - The hash value will be the key for the dict
        - Return the shorten URL
        - Use shorten URL as key to find original URL
        """
        self.urlDict = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        key = hash(longUrl)
        self.urlDict[key] = longUrl
        return key

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.urlDict[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))