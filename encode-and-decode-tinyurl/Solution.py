// https://leetcode.com/problems/encode-and-decode-tinyurl

class Codec:
    def __init__(self) -> None:
        self.d: Dict[str, str] = {}
        self.count: int = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        encode = str(self.count)
        self.d[encode] = longUrl

        return encode
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if self.d:
            return self.d.get(shortUrl)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))