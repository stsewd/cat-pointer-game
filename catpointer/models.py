from dataclasses import dataclass
from typing import Tuple


@dataclass
class Cat:
    x: int
    y: int
    # x, y, width, height
    drawing_area: Tuple[int, int, int, int]
    # x, y
    image_position: Tuple[int, int] = (0, 0)
    height: int = 16
    width: int = 16
    rigth: bool = False
    colkey: int = 5

    def move_left(self, x=2):
        self.x = max(
            self.x - x,
            self.drawing_area[0]
        )
        self.rigth = False

    def move_right(self, x=2):
        self.x = min(
            self.x + x,
            self.drawing_area[2] - self.width
        )
        self.rigth = True

    def move_up(self, y=2):
        self.y -= y

    def move_down(self, y=2):
        self.y += y

    @property
    def is_up(self):
        return self.y + self.height < self.drawing_area[3]


@dataclass
class Point:
    x: int
    y: int
