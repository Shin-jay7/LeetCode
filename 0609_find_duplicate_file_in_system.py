from __future__ import annotations
from typing import List
from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for data in paths:
            path, *files = data.split()
            for file in files:
                name, content = file.split('(')
                groups[content].append(path + '/' + name)

        return [g for g in groups.values() if len(g) > 1]


test = Solution()
test.findDuplicate(
     ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
    )
#  [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
