import pygame
import sys
import os

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from projectile import Shot, shot_group
from scoring import print_high_scores, update_high_scores


BLACK = (0, 0, 0)
FPS = 60
STARTING_SCORE = 0
ASTEROID_KILL_SCORE = 1


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Starting Asteroids!")
    name = input("What is your name?\n").strip()

    clock = pygame.time.Clock()
    dt = 0
    pygame.init()
    score = STARTING_SCORE

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    AsteroidField()

    Shot.containers = (shot_group, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BLACK)
        for d in drawable:
            d.draw(screen)

        time_elapsed = clock.tick(FPS)
        dt = time_elapsed/1000

        for u in updatable:
            u.update(dt)

        pygame.display.flip()

        for asteroid in asteroids:
            if asteroid.hit(player):
                print(f"You scored: {score}")
                update_high_scores(name, score)
                print_high_scores()
                sys.exit("Game Over!")

        for asteroid in asteroids:
            for shot in shot_group:
                if asteroid.hit(shot):
                    asteroid.split()
                    shot.kill()
                    score += ASTEROID_KILL_SCORE


if __name__ == "__main__":
    main()
