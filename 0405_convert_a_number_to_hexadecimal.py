from __future__ import annotations


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_chars, ans = "0123456789abcdef", []
        if num < 0:
            num += (1 << 32)

        while num:
            num, mod = divmod(num, 16)
            ans.append(hex_chars[mod])

        return "".join(reversed(ans))


class Solution:
    def toHex(self, num: int) -> str:
        # num >> 4 means num // 16 because 16 = 2**4
        # num & 15 means num % 15 and 15 is encoded in hex as "f" 
        return (
            self.toHex((num >> 4) & (2**28-1)) +
            "0123456789abcdef"[num & 15]
            if num else "0"
            ).lstrip("0") or "0"


test = Solution()
test.toHex(26)  # "1a"
