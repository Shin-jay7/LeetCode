from __future__ import annotations


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "")
        q, r = divmod(len(s), k)
        ans = s[:r].upper() if r else ""
        for _ in range(q):
            ans += "-" if ans else ""
            ans += s[r:r+k].upper()
            r += k
        return ans


test = Solution()
test.licenseKeyFormatting("5F3Z-2e-9-w", 4) # "5F3Z-2E9W"
