# Last updated: 30/07/2026, 20:31:28
1class Codec:
2    def __init__(self):
3        self.counter = 0
4        self.domain = "https://tinyurl.com"
5        self.d = {}
6
7    def encode(self, longUrl: str) -> str:
8        """Encodes a URL to a shortened URL.
9        """
10        self.counter += 1
11        self.d[self.counter] = longUrl
12
13        return f"{self.domain}/{self.counter}"
14
15    def decode(self, shortUrl: str) -> str:
16        """Decodes a shortened URL to its original URL.
17        """
18        code = shortUrl.split("/")[-1]
19        return self.d[int(code)]
20        
21
22# Your Codec object will be instantiated and called as such:
23# codec = Codec()
24# codec.decode(codec.encode(url))