from __future__ import annotations


class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        bulbs = [1]*n
        # print(bulbs)
        for round in range(2, n):
            for i in range(n):
                if i % round == round-1:
                    bulbs[i] ^= 1
            # print(bulbs)

        bulbs[-1] ^= 1
        # print(bulbs)

        return sum(bulbs)


test = Solution()
test.bulbSwitch(4) # 2
