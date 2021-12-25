from __future__ import annotations
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ["Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i) for i in range(1, n+1)]


test = Solution()
test.fizzBuzz(15)
# ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
