from __future__ import annotations


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dic = {cha: 1 for cha in p}
        cnt = 1  # Count continued chars
        for cha_i, cha_j in zip(p, p[1:]):
            cnt = cnt+1 if (ord(cha_j) - ord(cha_i)) % 26 == 1 else 1
            dic[cha_j] = max(dic[cha_j], cnt)
        return sum(dic.values())


test = Solution()
test.findSubstringInWraproundString("zab")  # 6
