import pygame
from pygame import Color, Surface
from loguru import logger

from car import Car
from road import Road

# constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
CANVAS_WIDTH = WINDOW_WIDTH / 2
CANVAS_HEIGHT = WINDOW_HEIGHT
CAR_WIDTH = 30
CAR_HEIGHT = 50


def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("02 Road Definition")
    clock = pygame.time.Clock()

    canvas = Surface((CANVAS_WIDTH, CANVAS_HEIGHT))
    road = Road(CANVAS_WIDTH / 2, CANVAS_WIDTH * 0.9)
    car = Car(
        road.get_lane_center(1),
        CANVAS_HEIGHT - 2 * CAR_HEIGHT,
        CAR_WIDTH,
        CAR_HEIGHT,
    )
    car.store()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    car.reset()

        window.fill(Color("darkgray"))
        canvas.fill(Color("lightgray"))

        car.update()
        car.draw(canvas)

        window.blit(canvas, ((WINDOW_WIDTH - CANVAS_WIDTH) / 2, 0))

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Program terminated by user.")
    except Exception as e:
        logger.exception("An error occurred in the main loop: {}", e)
    finally:
        pygame.quit()
        logger.info("Pygame quit successfully.")
