import pygame
from pygame import Color, Surface
from loguru import logger

from car import Car

# constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
ROAD_WIDTH = WINDOW_WIDTH / 2
ROAD_HEIGHT = WINDOW_HEIGHT
CAR_WIDTH = 30
CAR_HEIGHT = 50

def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("01 Car Driving Mechanics")
    clock = pygame.time.Clock()

    car = Car((ROAD_WIDTH - CAR_WIDTH) / 2, 50, CAR_WIDTH, CAR_HEIGHT)
    road = Surface((ROAD_WIDTH, ROAD_HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(Color("darkgray"))

        road.fill(Color("lightgray"))

        car.update()
        car.draw(road)

        window.blit(road, ((WINDOW_WIDTH - ROAD_WIDTH) / 2, 0))

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
