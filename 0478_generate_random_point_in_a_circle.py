from __future__ import annotations
from typing import List
import random
import math


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        while True:
            x, y = random.uniform(-self.r, self.r), random.uniform(-self.r, self.r)
            if x**2 + y**2 <= self.r**2:
                return [x + self.x_center, y + self.y_center]


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        area = math.pi * self.r**2
        R = math.sqrt(random.uniform(0, area) / math.pi)
        theta = random.uniform(0, 360)
        return [self.x + R * math.cos(theta), self.y + R * math.sin(theta)]
