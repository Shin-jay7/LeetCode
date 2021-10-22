from __future__ import annotations


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r = num
        while r*r > num:
            # https://qiita.com/PlanetMeron/items/09d7eb204868e1a49f49
            r = (r + num/r) // 2
        return r*r == num


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        OP is simply trying to set every bit to 1 starting from most significant
        one and if root^2 with that bit set to 1 becomes larger than given num, 
        the bit is unset back to 0. Assuming that the num is an unsigned 32-bit 
        integer, numbers starting from 2^16 won't fit when squared, which is why
        bit mask starts from 2^15 so the max possible number would be 2^16-1.
        """
        root = 0
        bit = 1 << 15

        while bit > 0:
            root |= bit
            if root > num//root:
                root ^= bit
            bit >>= 1

        return root*root == num


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # 1 + 3 + 5 + ... + (2n-1)
        i = 1
        while num > 0:
            num -= i
            i += 2

        return num == 0


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num

        while left <= right:
            mid = left + (right-left) // 2
            if mid**2 == num:
                return True
            elif mid**2 > num:
                right = mid - 1
            else:
                left = mid + 1

        return False
