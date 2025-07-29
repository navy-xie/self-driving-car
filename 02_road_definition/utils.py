import math
import pygame

def draw_dashed_line(surface, color, start_pos, end_pos, dash_length=10, gap_length=5):
    x1, y1 = start_pos
    x2, y2 = end_pos
    dx = x2 - x1
    dy = y2 - y1
    distance = math.sqrt(dx**2 + dy**2)
    
    dash_and_gap = dash_length + gap_length
    num_segments = int(distance / dash_and_gap)

    for i in range(num_segments + 1):
        start_x_segment = x1 + (dx * i * dash_and_gap) / distance
        start_y_segment = y1 + (dy * i * dash_and_gap) / distance
        
        end_x_segment = x1 + (dx * (i * dash_and_gap + dash_length)) / distance
        end_y_segment = y1 + (dy * (i * dash_and_gap + dash_length)) / distance
        
        # Ensure the segment doesn't go beyond the end point
        if math.sqrt((end_x_segment - x1)**2 + (end_y_segment - y1)**2) > distance:
            end_x_segment = x2
            end_y_segment = y2

        pygame.draw.line(surface, color, (start_x_segment, start_y_segment), (end_x_segment, end_y_segment))
        