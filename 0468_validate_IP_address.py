from __future__ import annotations


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def is_IPv4(chars):
            try:
                return str(int(chars)) == chars and 0 <= int(chars) <= 255
            except ValueError:
                return False

        def is_IPv6(chars):
            try:
                return int(chars, 16) >= 0 and 1 <= len(chars) <= 4
            except ValueError:
                return False

        if queryIP.count(".") == 3 and\
           all(is_IPv4(chars) for chars in queryIP.split(".")):
            return "IPv4"
        elif queryIP.count(":") == 7 and\
           all(is_IPv6(chars) for chars in queryIP.split(":")):
            return "IPv6"
        return "Neither"


test = Solution()
test.validIPAddress("172.16.254.1")  # "IPv4"
