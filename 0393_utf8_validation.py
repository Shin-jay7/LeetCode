from __future__ import annotations
from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        cnt = 0 # 10xxxxxxであるbyteが必要な件数

        for byte in data:
            if 128 <= byte <= 191:
                # 10xxxxxx
                if not cnt:
                    return False
                cnt -= 1
            else:
                if cnt:
                    return False
                if byte < 128:
                    # 10000000未満
                    continue
                elif byte < 224:
                    # 11100000未満
                    cnt = 1
                elif byte < 240:
                    # 11110000未満
                    cnt = 2
                elif byte < 248:
                    # 11111000未満
                    cnt = 3
                else:
                    return False

        return cnt == 0


test = Solution()
test.validUtf8([197,130,1]) # True

test = Solution()
test.validUtf8([235,140,4]) # False

test = Solution()
test.validUtf8([255]) # False

test = Solution()
test.validUtf8([237]) # False

test = Solution()
test.validUtf8([145]) # False

test = Solution()
test.validUtf8([240,162,138,147,145]) # False

test = Solution()
test.validUtf8([250,145,145,145,145]) # False
