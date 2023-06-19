import pygame

class Cell:
    def __init__(self, x, y, squareSize, isAlive = False):
        self.pos = (x, y)
        self.isAlive = isAlive
        self.gridCell = pygame.rect(x, y, squareSize, squareSize)