from __future__ import annotations
from functools import reduce
from operator import xor


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = reduce(xor, nums) 
        # ansのxorになる。他は2回出てくるので相殺される。
        # テストケースの場合、sは6になる。
        nz = s & (s-1) ^ s
        # s & (s-1)を使うと、最後の1を外すことができる。
        # 例えば、s = 110100のケースでは、s & (s-1) = 110000 となる。
        # その結果とsのxorをすることで最後の１を取り出すことができる。
        # s & (s-1) ^ s = 100
        # ちなみにテストケースの場合は、２進法で10、つまり十進法で2となる
        num1 = reduce(xor, filter(lambda n: n & nz, nums))
        # ２進法で10が存在するものだけでxorしてる。なぜ？？？
        # テストケースの場合は、２進法で11、つまり十進法で3となる

        return(num1, s ^ num1)
        # print(num1, s ^ num1)
        # テストケースの場合は、最終的に3と5が残る
        # なぜこうすれば答えとなるの？


test = Solution()
test.singleNumber([1,2,1,3,2,5]) # [3,5]
