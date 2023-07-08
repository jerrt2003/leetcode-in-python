# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

from typing import List
from concurrent import futures


class Solution:
    def crawl(self, startUrl: str, htmlParser: "HtmlParser") -> List[str]:
        visited = set([startUrl])

        with futures.ThreadPoolExecutor(max_workers=16) as executor:
            tasks = deque([executor.submit(htmlParser.getUrls, startUrl)])
            while tasks:
                for url in tasks.popleft().result():
                    if url not in visited and self.get_hostname(
                        startUrl
                    ) == self.get_hostname(url):
                        visited.add(url)
                        tasks.append(executor.submit(htmlParser.getUrls, url))

        return visited

    def get_hostname(self, url) -> str:
        return url.split("/")[2]
