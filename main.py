import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT


BLACK = (0, 0, 0)
FPS = 60


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(BLACK)
        pygame.display.flip()
        time_elapsed = clock.tick(FPS)
        dt = time_elapsed/1000


if __name__ == "__main__":
    main()
