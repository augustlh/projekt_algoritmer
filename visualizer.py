from sorting_algorithms import *
from values import *
import pygame
from typing import Callable

class Visualizer:
    def __init__(self, title : str) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.status = "Running"

    def tick(self, tickrate : int) -> None:
        self.clock.tick(tickrate)
        pygame.event.pump()

    def close(self) -> None:
        self.status = "Closed"
        pygame.quit()

    def await_closure(self) -> None:
        while self.status == "Running":
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.close()

    def await_keypress(self, key : str):
        while True:
            for event in pygame.event.get(eventtype = pygame.KEYDOWN):
                if pygame.key.name(event.key).lower() == key.lower(): return
            self.tick(60)
                
                    
          
    def bar_animation(self, algorithm : Callable, arr : list[float]) -> None:
        if algorithm == bubble_sort: tickrate = 0
        else: tickrate = 60
        for x, y in algorithm(arr):
            self.tick(tickrate)
            self.bar_visualize(x, y)

        #tegn grøn bar efter sort er færdig
        for i in range(len(x)):
            self.tick(240)
            color = (0,255,0)
            pygame.draw.rect(self.screen, color, (i * bar_width, height - x[i], bar_width, x[i]))   
            pygame.display.update()

    def bar_visualize(self, arr : list[float], index : int) -> None:
        self.screen.fill((0,0,0))
        for i in range(len(arr)):
            color = (255,255,255) if i != index else (255,0,0)
            pygame.draw.rect(self.screen, color, (i * bar_width, height - arr[i], bar_width, arr[i]))       
        pygame.display.update()
