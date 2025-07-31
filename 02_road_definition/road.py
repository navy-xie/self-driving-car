from pygame.math import Vector2
from pygame import Surface, Color
import pygame

from utils import draw_dashed_line


class Road:
    def __init__(self, center_x: float, width: float, lane_count: int = 3):
        self.center_x = center_x
        self.width = width
        self.lane_count = lane_count

        self.left = center_x - width / 2
        self.right = center_x + width / 2

        INFINITY = 1_000
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

    def draw(self, canvas: Surface, offset_y: float):
        line_width = 5
        dash_length = 20
        gap_length = 20
        line_color = Color("white")

        # draw board
        for border in self.borders:
            pygame.draw.line(canvas, line_color, 
                             (border[0].x, border[0].y + offset_y),
                             (border[1].x, border[1].y + offset_y),
                             line_width)

        # draw dash lines
        for i in range(self.lane_count - 1):
            x = self.left + self.width * (i + 1) / self.lane_count
            draw_dashed_line(canvas,
                             line_color,
                             (x, self.top + offset_y),
                             (x, self.bottom + offset_y),
                             dash_length, gap_length)
