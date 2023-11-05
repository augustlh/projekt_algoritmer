# August Leander Hedman
# augu1789@edu.nextkbh.dk
# NEXT Sukkertoppen, S3n    

# View-delen af MVC.

# Importer relevante biblioteker og funktioner osv. fra andre filer i programmet
from sorting_algorithms import *
from values import *
import pygame
from typing import Callable
import numpy as np

# Konstant
speed = 0.1

# Funktion for lineær interpolation (lerp) mellem to punkter, så der laves en animation
def lerp(pos, targetPos, speed):
    return pos + (targetPos - pos) * speed

# Klasse for at repræsentere en boks
class Box:
    def __init__(self, pos: np.ndarray, color: Tuple[int, int, int], size: Union[int, float], value: Union[int, float]) -> None:
        self.pos = pos
        self.size = size
        self.targetPos = pos
        self.color = color
        self.value = value

    def update(self) -> None:
        # Hvis self.targetPos != self.pos, så lerp
        if np.linalg.norm(self.pos - self.targetPos) > 0.1:
            self.pos = lerp(self.pos, self.targetPos, speed)

    def show(self, screen) -> None:
        pygame.draw.rect(screen,self.color, pygame.Rect(self.pos[0], self.pos[1], self.size, self.size))

        font = pygame.font.Font('freesansbold.ttf', int(self.size * 0.4) )
        text = font.render(str(self.value), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (self.pos[0] + self.size /2, self.pos[1] + self.size /2)
        screen.blit(text, textRect)

# Klassen, som er view-delen af MVC
class Visualizer:
    def __init__(self, title: str) -> None:
        # pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.status = "Running"
        self.font = pygame.font.Font(None, 36)

        self.algorithm = None

    def tick(self, tickrate : int) -> None:
        # pygame tick
        self.clock.tick(tickrate)
        pygame.event.pump()

    def close(self) -> None:
        # pygame close
        self.status = "Closed"
        pygame.quit()

    def await_closure(self) -> None:
        # while-loop for at holde vinduet åbent
        while self.status == "Running":
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.close()

    def await_keypress(self, key: str) -> None:
        # while-loop for at holde vinduet åbent indtil en given tast er trykket
        while True:
            for event in pygame.event.get(eventtype = pygame.KEYDOWN):
                if pygame.key.name(event.key).lower() == key.lower(): return

            text = self.font.render("Tryk c for at fortsætte", True, (255, 255, 255), (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (self.screen.get_width()/2, 25)
            self.screen.blit(text, textRect)
            pygame.display.update()
          
          
    def bar_animation(self, algorithm: Callable, arr: List[Union[int, float]]) -> None:
        if algorithm == merge_sort or radix_sort: tickrate = 120
        else: tickrate = 60

        self.algorithm = algorithm

        # For hver iteration af algoritmen visualiseres den nuværende tilstand af arrayet
        for x, y, z in algorithm(arr):
            self.tick(tickrate)
            self.bar_visualize(x, y, z)

        #tegn grøn bar efter sort er færdig
        bar_width = width / len(arr)
        for i in range(len(x)):
            self.tick(240)
            color = (0,255,0)
            pygame.draw.rect(self.screen, color, (i * bar_width, height - x[i], bar_width, x[i]))   
            pygame.display.update()

    def bar_visualize(self, arr: List[Union[int, float]], index: int, index2: int = -1) -> None:
        bar_width = width / len(arr) if len(arr) > 0 else width // n
        self.screen.fill((0,0,0))
        self.showName()
        for i in range(len(arr)):
            color = (255, 0, 0) if i == index else (0, 255, 0) if i == index2 else (255, 255, 255)
            pygame.draw.rect(self.screen, color, (i * bar_width, height - arr[i], bar_width, arr[i]))       
        pygame.display.update()

    def boxSort(self, algorithm: Callable, arr: List[Union[int, float]]) -> None:
        self.algorithm = algorithm
        n = len(arr) 

        # Beregner størrelsen af boksene og afstanden mellem dem
        boxDistance = 800 / n 
        boxSize = boxDistance * 0.8
        
        # Opretter en liste af bokse for hvert index i arrayet arr
        boxes = [Box(np.array([i * boxDistance, self.screen.get_height()/2 - boxSize/2]), (255, 255, 255), boxSize, arr[i]) for i in range(len(arr))]

        # For hver iteration af algoritmen, skal boksnene visualiseres og evt. bytte plads
        for x, y, z in algorithm(arr):
            if algorithm == stalin_sort: boxes = [Box(np.array([i * boxDistance, self.screen.get_height()/2 - boxSize/2]), (255, 255, 255), boxSize, arr[i]) for i in range(len(arr))]
            self.clock.tick(10)
            # Skal to bokse bytte plads?
            swap = x[y] != arr[y] or x[z] != arr[z] if algorithm != stalin_sort else False
        
            for i in range(len(boxes)):
                boxes[i].color = (0, 255, 0) if i == y else (255, 0, 0) if i == z else (255, 255, 255)
            self.showBoxes(boxes, algorithm)
        
            if swap:
                self.swapBoxes(y, z, boxes)
                arr[y], arr[z] = arr[z], arr[y]

    # Metode, der tegner alle bokse på skærmen
    def showBoxes(self, boxes: List[Box], algorithm: Callable = None) -> None:
        self.screen.fill((0, 0, 0))
        self.showName()
        for box in boxes:
            box.show(self.screen)
        pygame.display.update()
    
    # Metode, som bytter plads på to bokse ved et while loop og lerping
    def swapBoxes(self, boxIndex: int, boxIndex2: int, boxes: List[Box]):
        # Sæt targetPos for de to bokse
        boxes[boxIndex].targetPos, boxes[boxIndex2].targetPos = boxes[boxIndex2].pos, boxes[boxIndex].pos

        # Kør så længe boksene ikke er nået til deres targetPos (lerping)
        while np.linalg.norm(boxes[boxIndex].pos - boxes[boxIndex].targetPos) > 0.1 and np.linalg.norm(boxes[boxIndex2].pos - boxes[boxIndex2].targetPos) > 0.1:
            self.screen.fill((0, 0, 0))
            self.showName()
            self.clock.tick(60)
            boxes[boxIndex].update()
            boxes[boxIndex2].update()
            self.showBoxes(boxes)
            pygame.display.update()

        boxes[boxIndex], boxes[boxIndex2] = boxes[boxIndex2], boxes[boxIndex]
    # Metode, som viser navnet på den algoritme, der bliver kørt        
    def showName(self):
        text = self.font.render(str(self.algorithm.__name__), True, (255, 255, 0), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (50 + len(str(self.algorithm)), 25)
        self.screen.blit(text, textRect)
   