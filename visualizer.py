from sorting_algorithms import *
from values import *
import pygame
from typing import Callable
import numpy as np

class Visualizer:
    def __init__(self, title : str) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.status = "Running"

        self.font = pygame.font.Font(None, 36)

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
        elif algorithm == mergeSort or augussySort: tickrate = 120
        else: tickrate = 60
        for x, y, z in algorithm(arr):
            self.tick(tickrate)
            self.bar_visualize(x, y, z)

        #tegn grøn bar efter sort er færdig
        for i in range(len(x)):
            self.tick(240)
            color = (0,255,0)
            pygame.draw.rect(self.screen, color, (i * bar_width, height - x[i], bar_width, x[i]))   
            pygame.display.update()

    def bar_visualize(self, arr : list[float], index : int, index2 = -1) -> None:
        bar_width = width / len(arr)
        self.screen.fill((0,0,0))
        for i in range(len(arr)):
            #color = (255,255,255) if i != index else (255,0,0)
            color = (255, 0, 0) if i == index else (0, 255, 0) if i == index2 else (255, 255, 255)
            pygame.draw.rect(self.screen, color, (i * bar_width, height - arr[i], bar_width, arr[i]))       
        pygame.display.update()

    
    def box_animation(self, algorithm : Callable, arr : list[float]) -> None:
        tickrate = 2
        self.box_visualize(arr, -1, -1)
        for x, y, z in algorithm(arr):
            self.tick(tickrate)
            self.box_visualize(x,y,z)

    def box_visualize(self, arr : list[float], index2 : int, index : int) -> None:
        self.screen.fill((0,0,0))
        l = 40
        x_coordinates = np.linspace(0, width - l, len(arr))
        for i in range(len(arr)):
            color = (255, 0, 0) if i == index else (0, 255, 0) if i == index2 else (255, 255, 255)
            pygame.draw.rect(self.screen, color, (x_coordinates[i], height/2 - l/2, l, l))

            text = self.font.render(str(arr[i]), True, (0,0,0))
            textRect = text.get_rect()
            textRect.center = (x_coordinates[i] + l /2, height/2)

            self.screen.blit(text, textRect)

            pygame.time.wait(100)
        pygame.display.update()
        
