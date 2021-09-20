from __future__ import annotations
import operator


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(map(operator.eq, secret, guess))
        both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
        return str(bulls) + "A" + str(both-bulls) + "B"


test = Solution()
test.getHint("1807", "7810")
