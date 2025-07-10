from pygame.math import Vector2
from pygame import Surface


class Road:
    def __init__(self, center_x: float, width: float, lane_count: int = 3):
        self.center_x = center_x
        self.width = width
        self.lane_count = lane_count

        self.left = center_x - width / 2
        self.right = center_x + width / 2

        INFINITY = 1_000_000
        self.top = -INFINITY
        self.bottom = INFINITY

        self.left_top = Vector2(self.left, self.top)
        self.right_top = Vector2(self.right, self.top)
        self.left_bottom = Vector2(self.left, self.bottom)
        self.right_bottom = Vector2(self.right, self.bottom)

        self.borders = [
            (self.left_top, self.left_bottom),
            (self.right_top, self.right_bottom),
        ]

    def get_lane_center(self, lane_index: int) -> float:
        if lane_index < 0 or lane_index >= self.lane_count:
            raise ValueError("Lane index out of bounds")
        lane_width = self.width / self.lane_count

        return self.left + (lane_index + 0.5) * lane_width

    def draw(self, canvas: Surface): ...
