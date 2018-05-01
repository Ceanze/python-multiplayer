import pygame
import sys
import time
import random
import threading
from client import *
from player import *

from pygame.locals import *

MULTIPLAYER = True

# Pygame things
FPS = 60
pygame.init()
fpsClock=pygame.time.Clock()

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()
surface.fill((255,255,255))
clock = pygame.time.Clock()

pygame.key.set_repeat(1, 40)

if __name__ == '__main__':
    color = (0, 0, 0)
    player = Player([320, 300])
    if MULTIPLAYER:
        client = Client("127.0.0.1", 8080)
        client.connect()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if MULTIPLAYER:
                    client.quit()
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()
            if keys[K_SPACE]:
                player.jump()
            if keys[K_d]:
                player.move([1, 0])
            if keys[K_a]:
                player.move([-1, 0])
            if keys[K_ESCAPE]:
                if MULTIPLAYER:
                    client.quit()
                pygame.quit()
                sys.exit()


        surface.fill((255,255,255))
        player.update()
        player.draw(surface)

        if MULTIPLAYER:
            for p in client.getPlayers():
                p[1].update()
                p[1].draw(surface)

        screen.blit(surface, (0,0))

        pygame.display.flip()
        pygame.display.update()
        player.update()
        if MULTIPLAYER:
            client.update(player.getPosition())

        fpsClock.tick(FPS)