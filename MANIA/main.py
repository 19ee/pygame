import pygame
import background
from time import time

# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
dt = 0
_FPS = 120

num_of_keys = 4
keys = ["D","F","J","K"]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    background.draw_background(screen, num_of_keys)
    background.draw_keys(screen, keys)

    # flip() the display to put your work on screen
    pygame.display.flip()
    #print(player_pos)

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(_FPS) / 1000

pygame.quit()
