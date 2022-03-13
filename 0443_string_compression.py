from __future__ import annotations
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        while idx < len(chars):
            cnt = 1
            while idx+1 < len(chars) and chars[idx] == chars[idx+1]:
                cnt += 1
                del chars[idx+1]
            if cnt > 1:
                for char in str(cnt):
                    chars.insert(idx+1, char)
                    idx += 1
            idx += 1

        return len(chars)
