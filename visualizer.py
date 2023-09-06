from sorting_algorithms import *
from values import *
import pygame, random
from typing import Callable

class Visualizer:
    def __init__(self, title : str) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.status = "Running"

    def tick(self : None, tickrate : int) -> None:
        self.clock.tick(tickrate)
        pygame.event.pump()

    def close(self : None) -> None:
        self.status = "Closed"
        pygame.quit()

    def await_closure(self : None) -> None:
        while self.status == "Running":
            self.tick(60)
          

    def bar_animation(self : None, algorithm : Callable, arr : list[float]) -> None:
        for x, y in algorithm(arr):
            self.tick(60)
            self.bar_visualize(x, y)
            
        

    def bar_visualize(self, arr : list[float], index : int) -> None:
        self.screen.fill((0,0,0))
        for i in range(len(arr)):
            color = (255,255,255) if i != index else (255,0,0)
            pygame.draw.rect(self.screen, color, (i * bar_width, height - arr[i], bar_width, arr[i]))       
        pygame.display.update()
        

