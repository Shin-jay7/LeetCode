from __future__ import annotations
from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stickers.sort(key=lambda x: len(x), reverse=True)
        temp = []
        for sticker in stickers:
            temp1 = {}
            for st in sticker:
                temp1[st] = temp1.get(st, 0) + 1
            temp.append(temp1)
        stickers = temp
        memo = {'': 0}

        def dfs(target):
            if target in memo:
                return memo[target]
            ans = float('inf')
            for sticker in stickers:
                if target[0] not in sticker:
                    continue
                target_new = target
                for st in sticker:
                    target_new = target_new.replace(st, '', sticker[st])
                if target_new == '':
                    ans = 1
                    break
                elif target_new != target:
                    ans = min(ans, dfs(target_new) + 1)
            memo[target] = ans
            return ans
        
        ans = dfs(target)
        if ans == float('inf'):
            return -1
        return ans
