from __future__ import annotations
from typing import List
import operator


# Since there are no lakes, every pair of neighbour cells with different values
# is part of the perimeter (more precisely, the edge between them is). 
# So just count the differing pairs, both horizontally and vertically 
# (for the latter I simply transpose the grid).
class Solution(object):
    def islandPerimeter(self, grid):
        grid_ext = ['0' + ''.join(str(x) for x in row) + '0' for row in grid]
        grid_trans = list(map(list, zip(*grid)))
        grid_ext += [ '0' + ''.join(str(x) for x in row) + '0' for row in grid_trans ]                
        return sum(row.count('01') + row.count('10') for row in grid_ext)


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        return sum(sum(map(operator.ne, [0] + row, row + [0]))
                   for row in grid + map(list, zip(*grid)))
