from sorting_algorithms import *
import pygame, random

class Visualizer:
    def __init__(self, title, size):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        

    def animate_bars(self, tickrate):
        pass

    def draw_bars(self):
        pass