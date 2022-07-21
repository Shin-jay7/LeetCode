from __future__ import annotations
import string
import random


class Codec:
    chars = string.ascii_letters + string.digits

    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}

    def encode(self, longUrl: str) -> str:
        while longUrl not in self.url_to_code:
            code = ''.join(random.choice(Codec.chars) for _ in range(6))
            if code not in self.code_to_url:
                self.code_to_url[code] = longUrl
                self.url_to_code[longUrl] = code
            return 'http://tinyurl.com/' + self.url_to_code[longUrl]

    def decode(self, shortUrl: str) -> str:
        return self.code_to_url[shortUrl[-6:]]
