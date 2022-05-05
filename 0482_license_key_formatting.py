from __future__ import annotations


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()[::-1]
        return '-'.join(s[i:i+k] for i in range(0, len(s), k)[::-1])


test = Solution()
test.licenseKeyFormatting("5F3Z-2e-9-w", 4) # "5F3Z-2E9W"
