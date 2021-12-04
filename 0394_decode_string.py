from __future__ import annotations
from string import ascii_lowercase


class Solution:
    def decodeString(self, s: str) -> str:
        stack, cnt, chars = [], 0, ""

        for char in s:
            if char == "[":
                stack.append(chars)
                stack.append(cnt)
                chars, cnt = "", 0
            elif char == "]":
                num = stack.pop()
                prev_chars = stack.pop()
                chars = prev_chars + num * chars
            elif char.isdigit():
                cnt = cnt*10 + int(char)
            else:
                chars += char

        return chars
