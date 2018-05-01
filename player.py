import pygame
from physics import *

class Box:

    def __init__(self, position, color, size):
        self.color = color
        self.size = size
        self.position = position
        self.p = pygame.rect.Rect(position, (self.size, self.size))

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.p)

    def setPosition(self, position):
        self.p = pygame.rect.Rect(position, (self.size, self.size))



class Player:

    def __init__(self, position, maxVelocity = 10):
        self.phys = Physics(position, maxVelocity)
        self.box = Box(position, (0, 0, 0), 10)
        
    def draw(self, window):
        self.box.draw(window)

    def update(self):
        self.phys.update(1)
        self.box.setPosition(self.phys.getPosition())

    def move(self, direction):
        self.phys.move(direction)

    def setPosition(self, position):
        self.phys.setPosition(position)

    def jump(self):
        self.phys.jump()

    def getPosition(self):
        return self.phys.getPosition()