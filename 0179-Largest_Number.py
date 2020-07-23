from __future__ import annotations


class LargerNumSortingLogic(str):
    def __lt__(x, y):
        return x+y > y+x
    # ex.) In case [3,34], "343" > "334" returns True

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans = "".join(sorted(map(str, nums), key=LargerNumSortingLogic))
        return "0" if ans[0] == "0" else ans


test = Solution()
test.largestNumber([10,2]) # "210"

test = Solution()
test.largestNumber([3,30,34,5,9]) # "9534330"
