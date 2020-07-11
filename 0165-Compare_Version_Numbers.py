from __future__ import annotations


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))
        l1, l2 = len(v1), len(v2)
        if l1 > l2:
            v2 += [0]*(l1-l2)
        elif l1 < l2:
            v1 += [0]*(l2-l1)

        for i in range(max(l1, l2)):
            if v1[i] > v2[i]:
                return 1
                # print(1)
                # return
            elif v1[i] < v2[i]:
                return -1
                # print(-1)
                # return

        return 0
        # print(0)
        # return


test = Solution()
test.compareVersion("0.1", "1.1") # -1

test = Solution()
test.compareVersion("1.0.1", "1") # 1

test = Solution()
test.compareVersion("7.5.2.4", "7.5.3") # -1

test = Solution()
test.compareVersion("1.01", "1.001") # 0

test = Solution()
test.compareVersion("1.0", "1.0.0") # 0

# test = Solution()
# test.compareVersion()
