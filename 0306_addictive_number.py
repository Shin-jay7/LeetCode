from __future__ import annotations


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        length = len(num)
        if length < 3:
            return False

        for i in range(1, length//2+1):
            if num[:i] != str(int(num[:i])):
                continue
            for j in range(i+1, length):
                first, second, remaining = num[:i], num[i:j], num[j:]
                if second != str(int(second)):
                    continue
                while remaining:
                    third = str(int(first) + int(second))
                    if not remaining.startswith(third):
                        break
                    first = second
                    second = third
                    remaining = remaining[len(third):]
                if not remaining:
                    return True

        return False

