from sorting_algorithms import *
from values import *
import pygame, random

class Visualizer:
    def __init__(self, title):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.status = "Running"

    def tick(self):
        self.clock.tick(60)
        pygame.event.pump()

    def close(self):
        self.status = "Closed"
        pygame.quit()

    def await_closure(self):
        while self.status == "Running":
            self.tick()


    def bar_animation(self, algorithm, arr):
        for x in algorithm(arr):
            self.tick()
            self.visualize(x)

    def visualize(self, arr):
        self.screen.fill((255,255,255))
        for i in range(len(arr)):
            pygame.draw.rect(self.screen, (0,0,0), (i * bar_width, height - arr[i], bar_width, arr[i]))
        pygame.display.update()

