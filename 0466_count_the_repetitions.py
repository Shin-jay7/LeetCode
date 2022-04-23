from __future__ import annotations


# https://leetcode.com/problems/count-the-repetitions/discuss/372230/Python-don't-look-at-words-look-at-chars-in-two-virtual-repeating-strings-detailed-explanation
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        d, i, j = {}, 0, 0
        # cnt = 1

        while i < len(s1) * n1:
            # print(cnt)
            i_mod, j_mod = i % len(s1), j % len(s2)
            if s1[i_mod] == s2[j_mod]:
                if (i_mod, j_mod) not in d:
                    d[(i_mod, j_mod)] = (i, j)
                else:
                    d1, d2 = i - d[(i_mod, j_mod)][0], j - d[(i_mod, j_mod)][1]
                    k = (len(s1) * n1 - i) // d1
                    i += k * d1
                    j += k * d2
                    # print("d1, d2, k")
                    # print(d1, d2, k)
                j += 1 and i < len(s1) * n1
            i += 1
            # cnt += 1
            # print("d, i, j")
            # print(d, i, j)

        return j // (len(s2) * n2)


test = Solution()
test.getMaxRepetitions("acb", 4, "ab", 2) # 2

test = Solution()
test.getMaxRepetitions("acb", n1 = 1, s2 = "acb", n2 = 1) # 1
