from __future__ import annotations

num1 = 1_00_000

print(num1)

#################################

from __future__ import annotations
class Point:
    x: float
    y: float
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y